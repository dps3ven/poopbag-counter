import mysql.connector
import os

## sourced from environment
mydb = mysql.connector.connect(
  host=(os.environ["database_host"]),
  user=(os.environ["database_user"]),
  password=(os.environ["database_user_password"])
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE {}".format(os.environ["database_name"]))