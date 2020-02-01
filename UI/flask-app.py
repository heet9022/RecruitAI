# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask, request, render_template
import login 
import json
import crud

# Run crud module
crud

# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/') 
def index(): 

    # with open('../Sample_Data/profiles.json') as f:
    #     data = json.load(f)

    data = crud.readDB()
    
    print(data)
    return render_template("index.html", data = data)

# @app.route('/submit')
# def submit():

#     return 'OK'
  
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug = True) 