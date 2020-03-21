import mysql.connector
import logging
import re

logger = logging.getLogger()

# CREATE TABLE `recruitai`.`profiles` ( `id` INT(50) NOT NULL AUTO_INCREMENT , `category` VARCHAR(100) NOT NULL , `url` VARCHAR(100) NOT NULL , `image_url` VARCHAR(500) NOT NULL , `about` VARCHAR(900) NOT NULL , `experience` VARCHAR(1000) NOT NULL , `name` VARCHAR(500) NOT NULL , `title` VARCHAR(600) NOT NULL , `location` VARCHAR(600) NOT NULL , `skills` VARCHAR(900) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;


class DatabaseConnector:

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="recruitai"
    )

    my_database = db_connection.cursor()

    def insertDB(self, category, URl, image_url, about, experience, name, title, location, skills):

        logger.info("INSERTING INTO Database...........")
        sql = "INSERT INTO `profiles`(`category`, `url`, `image_url`, `about`, `experience`, `name`, `title`, `location`, `skills`) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
        val = (category, URl, image_url, about,
               experience, name, title, location, skills)
        self.my_database.execute(sql, val)
        logger.info(".........Data inserted Successfully !")
        self.db_connection.commit()

    def readDB(self):

        self.my_database.execute(
            "SELECT * FROM profiles WHERE 1 LIMIT 10")

        myresult = self.my_database.fetchall()

        profiles = []  

        for x in myresult:

            profile = {}  

            profile['id'] = x[0]
            profile['category'] = x[1]
            profile['url'] = x[2]
            profile['image-url'] = x[3]
            profile['about'] = x[4]
            profile['experience'] = x[5]
            profile['name'] = x[6]
            profile['title'] = x[7]
            profile['location'] = x[8]
            profile['skills'] = self.convert_skills_to_array(x[9])

            profiles.append(profile)

        return profiles

    def convert_skills_to_array(self, skills):

        data = []
        data = skills.split('\\n')
        print("data: ", data)
        new_data = []
        for i in range(len(data)):
            data[i] = data[i].strip()
            data[i] = re.sub(r'[^a-zA-Z\s]', r'', data[i])
            if(data[i].isspace() or data[i] == '' or  data[i] == "','"):
                continue
            else:
                new_data.append(data[i])

        print()
        print("new_data: ",new_data)
        print()
        return new_data

    def search_query(self, job_category, location):
        query = "SELECT * FROM `profiles` WHERE location LIKE '%" + \
            location + "%' AND title LIKE '%" + job_category + "%'"
        self.my_database.execute(query)
        myresult = self.my_database.fetchall()

        profiles = []  # array of profiles # list

        for x in myresult:

            profile = {}  # json of each profile # dict

            profile['id'] = x[0]
            profile['category'] = x[1]
            profile['url'] = x[2]
            profile['image-url'] = x[3]
            profile['about'] = x[4]
            profile['experience'] = x[5]
            profile['name'] = x[6]
            profile['title'] = x[7]
            profile['location'] = x[8]
            profile['skills'] = self.convert_skills_to_array(x[9])

            profiles.append(profile)

        return profiles


if __name__ == "__main__":

    obj = DatabaseConnector()
    obj.insertDB("category", "url", "image_url", "about",
                 "exp", "name", "title", "loc", "skills")
