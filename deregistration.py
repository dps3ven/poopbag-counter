import mysql.connector
import os

## sourced from environment
print("What is your dog's name?")
dogname = str(input())
mydb = mysql.connector.connect(
  host=(os.environ["database_host"]),
  user=(os.environ["database_user"]),
  password=(os.environ["database_user_password"])
)
mydb.database=(os.environ["database_name"])
mycursor = mydb.cursor()
message = ('DELETE FROM Bags WHERE DogName="{dogname}"'.format(dogname=dogname))
mycursor.execute(message)
mydb.commit()