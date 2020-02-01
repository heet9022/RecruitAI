import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="recruitai"
)
my_database = db_connection.cursor()

profiles = [] # array of profiles # list
profile = {} # json of each profile # dict

def insertDB(name, location, skills, exp, about, title):

    print(".............INSERTING INTO Database...........")
    sql = "INSERT INTO `profiles`( `name`, `location`, `skills`, `exp`, `about`, title) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, location, skills, exp, about, title)
    my_database.execute(sql, val)

    db_connection.commit()

def readDB():

    my_database.execute("SELECT * FROM profiles")

    myresult = my_database.fetchall()

    for x in myresult:
        
        profile = {}
        profile['id'] = x[0]
        profile['name'] = x[1]
        profile['location'] = x[2]

        profile['skills'] = convert_skills_to_array(x[3])
        
        profile['experience'] = x[4]
        profile['about'] = x[5]
        profile['title'] = x[6]
        
        profiles.append(profile)
        # print(profiles)

    return profiles

def convert_skills_to_array(skills):

    data = []
    data = skills.split('\n')
    new_data=[]
    for i in range(len(data)):
        data[i] = data[i].strip()
        if(data[i].isspace() or data[i]==''):
            continue
        else:
            new_data.append(data[i])
    
    return new_data
        
# readDB()