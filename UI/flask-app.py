# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask, request, render_template
# import login 
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
    script_activate = 0 
    print(data)
    return render_template("index.html", data = data, script_activate = script_activate)

@app.route('/submit', methods=['POST'])
def submit():

    if request.method == 'POST':
        location = request.form['location']
        skills = request.form['skills']

    # run ML script
    job_category = "Cloud Engineer" # data from ML
    result = crud.search_query(job_category, location)

    # script = '<script>location.href = "#";location.href = "#results";</script>'
    script_activate = 1 

    return render_template("index.html", data = result, script_activate = script_activate)

@app.route('/resume')
def resume():
    import resume_scraper
    print(resume_scraper.main_dict)
    script_activate = 1 
    return render_template("index.html", data = resume_scraper.main_dict, script_activate = script_activate)  
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(debug = True) 