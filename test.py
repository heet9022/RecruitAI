import mysql.connector


db_connection = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="recruitai"
)
my_database = db_connection.cursor()

def insertDB(name, location, skills, exp, about, title):
    
    sql = "INSERT INTO `profiles`( `name`, `location`, `skills`, `exp`, `about`, title) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, location, skills, exp, about, title)
    my_database.execute(sql, val)

    db_connection.commit()

# init_DB()

name = 'heet'
loc = "ind"
skills_string = "djkjdk"
main_exp_data = "exp"
main_about_string = "about"
title = "title"

insertDB(name, loc, skills_string, main_exp_data, main_about_string, title)