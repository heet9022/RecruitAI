from flask import Flask, jsonify, request, render_template

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from wordcloud import WordCloud
from sklearn.linear_model import SGDClassifier, LogisticRegression

import string
import re
import spacy
import pickle
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append('Scraper/')

from database_module import DatabaseConnector 


punctuations = string.punctuation
stop_words = spacy.lang.en.stop_words.STOP_WORDS
parser = English()
        
class Predictors(TransformerMixin):
    def transform(self, X, **transform_params):

        # Cleaning Text
        cleaned_text = [clean_text(text) for text in X]

        # complete_text = ''
        # for text in cleaned_text:
        #   complete_text += text
        # makeWordCloud(complete_text)

        return cleaned_text

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}

# Basic function to clean the text
def clean_text(text):

    text = str(text)
    text = text.replace('\\n', '\n')
    text = text.replace('\\t', '\n')
    text = text.replace('\\r', '\n')
    
    text = text.replace("'b", ' ')
    text = re.sub(' nan ', ' ', text)
    text = re.sub(r'\\x[0-9a-z]{2}', r' ', text)
    text = re.sub(r'[0-9]{2,}', r' ', text)
    text = re.sub('http\S+\s*', ' ', text)  # remove URLs
    text = re.sub('RT|cc', ' ', text)  # remove RT and cc
    text = re.sub('#\S+', ' ', text)  # remove hashtags
    text = re.sub('@\S+', ' ', text)  # remove mentions
    text = re.sub('[%s]' % re.escape(
        """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)  # remove punctuations
    text = re.sub('\s+', ' ', text)  # remove extra whitespace
    text.lower()
    text = re.sub(r'xx+', r' ', text)
    text = re.sub(r'XX+', r' ', text)

    return text.strip()

# Tokenizer function
def spacy_tokenizer(sentence):

    mytokens = parser(sentence)

    mytokens = [word.lemma_.lower().strip() if word.lemma_ !="-PRON-" else word.lower_ for word in mytokens]

    mytokens = [word for word in mytokens if word not in stop_words and word not in punctuations]

    return mytokens


# Vectorizer
bow_vector = CountVectorizer(tokenizer=spacy_tokenizer, ngram_range=(1, 1), max_features=3500)
tfidf_vector = TfidfVectorizer(tokenizer=spacy_tokenizer, max_features=3500)

classifier = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)




app = Flask(__name__)


@app.route('/')
def index():

    db = DatabaseConnector()
    return render_template("index.html")


@app.route('/classify', methods=['POST'])
def classify():

    data = request.args.get('data')
    # print(data)
    testing_data = pd.read_json(data)
    testing_data = testing_data.skills
    # print(testing_data)
    pickle_in = open('Classifier\Models\localmodel2.pickle', 'rb')
    pipe = pickle.load(pickle_in)
    predictions = pipe.predict(testing_data)
    result = []
    for prediction in predictions:
        d = {}
        d['class'] = str(prediction)
        result.append(d)

    return jsonify(result)

if __name__ == '__main__':
    
    app.run(debug=True)
