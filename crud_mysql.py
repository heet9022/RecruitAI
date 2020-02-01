import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="recruitai"
)
my_database = db_connection.cursor()

sql = "INSERT INTO `profiles`( `name`, `location`, `skills`, `exp`, `about`) VALUES (%s,%s,%s,%s,%s)"
val = ("John", "Highway 21", "python","about", "exp")
my_database.execute(sql, val)

db_connection.commit()