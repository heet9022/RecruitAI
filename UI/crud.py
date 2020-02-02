import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="recruitai"
)
my_database = db_connection.cursor()


def insertDB(name, location, skills, exp, about, title, image):

    print(".............INSERTING INTO Database...........")
    sql = "INSERT INTO `profiles`( `name`, `location`, `skills`, `exp`, `about`, title, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name, location, skills, exp, about, title, image)
    my_database.execute(sql, val)

    db_connection.commit()

def readDB():

    my_database.execute("SELECT * FROM profiles WHERE image IS NOT NULL LIMIT 10")

    myresult = my_database.fetchall()

    profiles = [] # array of profiles # list

    for x in myresult:

        
        profile = {} # json of each profile # dict

        profile['id'] = x[0]
        profile['name'] = x[1]
        profile['location'] = x[2]

        profile['skills'] = convert_skills_to_array(x[3])

        profile['experience'] = x[4]
        profile['about'] = x[5]
        profile['title'] = x[6]
        profile['image-url'] =x[7]

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


def search_query(job_category, location):
    query = "SELECT * FROM `profiles` WHERE location LIKE '%" + location + "%' AND title LIKE '%"+ job_category +"%'"
    my_database.execute(query)
    myresult = my_database.fetchall()

    profiles = [] # array of profiles # list

    for x in myresult:

        
        profile = {} # json of each profile # dict

        profile['id'] = x[0]
        profile['name'] = x[1]
        profile['location'] = x[2]

        profile['skills'] = convert_skills_to_array(x[3])

        profile['experience'] = x[4]
        profile['about'] = x[5]
        profile['title'] = x[6]
        profile['image-url'] =x[7]

        profiles.append(profile)
        # print(profiles)

    return profiles 

# readDB()
