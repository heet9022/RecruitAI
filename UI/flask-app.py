# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask, request, render_template

import json
import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="recruitai"
)
my_database = db_connection.cursor()




# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/') 
def index(): 
    with open('../Sample_Data/profiles.json') as f:
        data = json.load(f)
    print(data)
    return render_template("index.html", data = data)

@app.route('/submit')
def submit():
    sql = "INSERT INTO `profiles`( `name`, `location`, `skills`, `exp`, `about`) VALUES ('Deep','Mumbai','python','jhata','me')"
    # val = ("John", "Highway 21"
    my_database.execute(sql)

    db_connection.commit()
    return 'OK'
  
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug = True) 