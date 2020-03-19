from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

from sklearn import metrics
from wordcloud import WordCloud

import string
import re
import spacy
import en_core_web_sm
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# !python -m pip install spacy
# !python -m spacy download en

resumeDataSet = pd.read_csv('Data/resume_eda_linkedin2.csv', encoding='utf-8')
resumeDataSet = resumeDataSet[['Category', 'Resume']]

# print(resumeDataSet.info())
# print(resumeDataSet.Category.unique())
# print(resumeDataSet.Category.value_counts())



# Basic function to clean the text
def clean_text(text):

    # Removing spaces and converting text into lowercase

    text = text.replace('\\n', '\n')
    text = text.replace('\\t', '\n')
    text = text.replace('\\r', '\n')
    # text = text[2:-1] #remove 'b
    text = text.replace("'b", ' ')
    text = re.sub('nan ', ' ', text)
    text = re.sub(r'\\x[0-9a-z]{2}', r' ', text)
    text = re.sub(r'[0-9]{2,}', r' ', text)
    text = re.sub('http\S+\s*', ' ', text)  # remove URLs
    text = re.sub('RT|cc', ' ', text)  # remove RT and cc
    text = re.sub('#\S+', ' ', text)  # remove hashtags
    text = re.sub('@\S+', ' ', text)  # remove mentions
    text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)  # remove punctuations
    text = re.sub('\s+', ' ', text)  # remove extra whitespace
    text.lower()
    text = re.sub(r'xx+', r' ', text)
    text = re.sub(r'XX+', r' ', text)
    
    return text.strip()
  
# Visualization
def makeWordCloud(data):
    wc = WordCloud().generate(data)
    plt.figure(figsize=(15,15))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    

# Custom transformer using spaCy
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):

        # Cleaning Text
        cleaned_text = [clean_text(text) for text in X]

        # Visualization
        
        # complete_text = ''
        # for text in cleaned_text:
        #   complete_text += text  
        # makeWordCloud(complete_text)

        return cleaned_text

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}


# Create our list of punctuation marks
punctuations = string.punctuation

# Create our list of stopwords
nlp = en_core_web_sm.load()
stop_words = spacy.lang.en.stop_words.STOP_WORDS

# Load English tokenizer, tagger, parser, NER and word vectors
parser = English()

# Creating our tokenizer function
def spacy_tokenizer(sentence):

    # Creating our token object, which is used to create documents with linguistic annotations.
    mytokens = parser(sentence)

    # Lemmatizing each token and converting each token into lowercase
    # -PRON- is for personal pronouns
    mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]

    # Removing stop words
    mytokens = [ word for word in mytokens if word not in stop_words and word not in punctuations ]

    # return preprocessed list of tokens
    return mytokens


# Vectorizer
bow_vector = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1), max_features=3500)
tfidf_vector = TfidfVectorizer(tokenizer = spacy_tokenizer, max_features = 3500)

X = resumeDataSet['Resume'] # the features we want to analyze
ylabels = resumeDataSet['Category'] # the labels
X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.3)


# Debugger
class Debug(TransformerMixin):

    def transform(self, X):
        print(pd.DataFrame(X))
        print(X.shape)
        return X

    def fit(self, X, y=None, **fit_params):
        return self


# Classifiers

# classifier = OneVsRestClassifier(KNeighborsClassifier()) 
# classifier =  MultinomialNB()
classifier = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None) 
# classifier = LogisticRegression(n_jobs=1, C=1e5, max_iter=100,multi_class='multinomial', solver='saga', dual=False)  
# classifier = RandomForestClassifier()
# classifier = xgb.XGBClassifier(objective='multi:softmax')


# Create pipeline 
# pipe = Pipeline([('cleaner', predictors()),
#                  ('vectorizer', tfidf_vector),
#                 #  ('dbg', Debug()),
#                  ('classifier', classifier)])

# Model Generation
# pipe.fit(X_train, y_train)

# with open('Models/localmodel.pickle','wb') as f:
#     pickle.dump(pipe, f)

pickle_in = open('Models/localmodel.pickle', 'rb')
pipe = pickle.load(pickle_in)

# Predicting with a test dataset
predicted = pipe.predict(X_test)
# print(predicted)

# Model Accuracy
print("Classification Report:",  metrics.classification_report(y_test, predicted))

#Testing

testing_data = pd.read_csv('Data/resume_pdf_trimmed.csv', encoding='utf-8')
testing_data = testing_data.Resume

predictions = pipe.predict(testing_data)
print(predictions)

