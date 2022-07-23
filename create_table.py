import mysql.connector
import os

## sourced from environment
mydb = mysql.connector.connect(
  host=(os.environ["database_host"]),
  user=(os.environ["database_user"]),
  password=(os.environ["database_user_password"])
)
mydb.database=(os.environ["database_name"])
mycursor = mydb.cursor(buffered=True)
mycursor.execute("CREATE TABLE IF NOT EXISTS Bags (DogName varchar(255) NOT NULL PRIMARY KEY, InitialBags int, Remaining int NOT NULL);")
mydb.commit()