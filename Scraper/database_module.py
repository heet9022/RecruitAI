import mysql.connector
import logging

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

        my_database.execute(
            "SELECT * FROM profiles WHERE image IS NOT NULL LIMIT 10")

        myresult = my_database.fetchall()

        profiles = []  # array of profiles # list

        for x in myresult:

            profile = {}  # json of each profile # dict

            profile['id'] = x[0]
            profile['name'] = x[1]
            profile['location'] = x[2]

            profile['skills'] = convert_skills_to_array(x[3])

            profile['experience'] = x[4]
            profile['about'] = x[5]
            profile['title'] = x[6]
            profile['image-url'] = x[7]

            profiles.append(profile)
            # print(profiles)

        return profiles

    def convert_skills_to_array(self, skills):

        data = []
        data = skills.split('\n')
        new_data = []
        for i in range(len(data)):
            data[i] = data[i].strip()
            if(data[i].isspace() or data[i] == ''):
                continue
            else:
                new_data.append(data[i])

        return new_data

    def search_query(self, job_category, location):
        query = "SELECT * FROM `profiles` WHERE location LIKE '%" + \
            location + "%' AND title LIKE '%" + job_category + "%'"
        my_database.execute(query)
        myresult = my_database.fetchall()

        profiles = []  # array of profiles # list

        for x in myresult:

            profile = {}  # json of each profile # dict

            profile['id'] = x[0]
            profile['name'] = x[1]
            profile['location'] = x[2]

            profile['skills'] = convert_skills_to_array(x[3])

            profile['experience'] = x[4]
            profile['about'] = x[5]
            profile['title'] = x[6]
            profile['image-url'] = x[7]

            profiles.append(profile)
            # print(profiles)

        return profiles


if __name__ == "__main__":

    obj = DatabaseConnector()
    obj.insertDB("category", "url", "image_url", "about",
                 "exp", "name", "title", "loc", "skills")
