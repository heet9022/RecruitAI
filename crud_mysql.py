import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="recruitai"
)
my_database = db_connection.cursor()

sql = "INSERT INTO `profiles`( `name`, `location`, `skills`, `exp`, `about`) VALUES ('Deep','Mumbai','python','jhata','me')"
# val = ("John", "Highway 21"
my_database.execute(sql)

db_connection.commit()