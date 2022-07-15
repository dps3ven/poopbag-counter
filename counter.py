import os
from re import M
import signal
import mysql.connector
from build import re
import time
import sys

mydb = mysql.connector.connect(
  host="192.168.1.27", ## non routable suckkas

)
mycursor = mydb.cursor(buffered=True)

# mycursor.execute("CREATE DATABASE IF NOT EXISTS poopbags;") ## var

mydb.database = "poopbags" ## var this is use database

initial_bags = 24

# maybe reorder table is primary key
## id needs to be generated ????

# mycursor.execute("INSERT INTO dottiepetersonbags VALUES(1,NULL,25)") ## needs to be update to scale

# mycursor.execute("INSERT INTO dottiepetersonbags VALUES(2,NULL,25)") ## needs to be update to scale
# mycursor.execute(sql)
# mycursor.execute("INSERT INTO Bags VALUES('dottie',1,25) ON DUPLICATE KEY UPDATE") ## needs to be update to scale

# DOgID needs generated???

# mycursor.execute("INSERT IGNORE INTO Bags VALUES(3,'lola',1,25)") ## needs to be update to scale
# mycursor.execute("INSERT IGNORE INTO Bags VALUES(4,'ginger',1,25)") ## needs to be update to scale
# # mycursor.execute("INSERT IGNORE INTO Bags (DogName,BagRollAge,Remaining) VALUES('dottie',1,25)")
# # mycursor.execute("INSERT IGNORE INTO Bags (DogName,BagRollAge,Remaining) VALUES('lola',1,25)")
# # mycursor.execute("INSERT INTO Bags VALUES('lola',1,25)") ## needs to be update to scale
# mydb.commit()
# print(mycursor.rowcount, "record affected.")
# time.sleep(60)
# mycursor.execute("DROP TABLE Bags")
# mydb.commit()
# mycursor.execute("set @used := 3")
# set @used := 3;
# update bags set `age`='`age` + 1';
# update bags set `remaining`=`remaining` - @used;
# select * from bags;

# update bags set age = 1, remaining = 25 where id = 1;
# select * from bags;


def showtables():
  mycursor.execute("SHOW Tables;")
  for x in mycursor:
    print(x) 

def output():
  mycursor.execute("Select * FROM Bags;")
  for x in mycursor:
    print(x)


def showdatabases():
  mycursor.execute("SHOW DATABASES;")
  for x in mycursor:
    print(x) 

def createtable():
  mycursor.execute("CREATE TABLE IF NOT EXISTS Bags (DogName varchar(255) NOT NULL PRIMARY KEY, BagRollAge int, InitialBags int, Remaining int);")
  mydb.commit()

def desc_tables():
  print("here is the table")
  mycursor.execute("Describe Bags;")  
  for x in mycursor:
    print(x)

def registration(dogname):
  message = 'INSERT INTO Bags(DogName, BagRollAge, InitialBags, Remaining) VALUES ("{dogname}", 1, 24, 24);'.format(dogname=dogname)
  mycursor.execute(message)
  mydb.commit()

def new_bags(dogname):
  message = 'UPDATE Bags Set Remaining = 24 WHERE Dogname = "{dogname}";'.format(dogname=dogname)
  mycursor.execute(message)
  mydb.commit()

def update(dogname):
  print("How many bags used today?")
  bags_used_today = int(input())
  try:
    q='SET @BagsRemaining := ( @Remains - {bags_used_today});'.format(initial_bags=initial_bags,bags_used_today=bags_used_today)
    mycursor.execute('SET @Remains := (SELECT Remaining FROM Bags WHERE DogName = "{dogname}");'.format(dogname=dogname))
    mydb.commit()
    mycursor.execute(q)
    mydb.commit()
    mycursor.execute('SELECT Remaining from Bags')
    bags_left = mycursor.fetchone()[0]
  except:
    print("Registation Error")
    raise Exception("Verify Registration for {}".format(dogname))

  bags_left = bags_left - bags_used_today ## lazy and should be put into separate function
  print(bags_left)
  if bags_left >=2:
    mycursor.execute('UPDATE Bags SET BagRollAge = 1, Remaining = @BagsRemaining WHERE DogName = "{dogname}";'.format(dogname=dogname))
    mydb.commit()
  elif bags_left ==1:
    print("Warning: New Bag Roll Needed")
    mycursor.execute('UPDATE Bags SET BagRollAge = 1, Remaining = @BagsRemaining WHERE DogName = "{dogname}";'.format(dogname=dogname))
    mydb.commit()
  else:
    raise Exception("No More Bags Left - Warned You")  
  print("Bags left {} for {}".format(bags_left, dogname))



def getRemaingBags(dogname): ## precondition currently lives in update function
  message = ('Select Remaining FROM Bags WHERE DogName = "{dogname}";'.format(dogname=dogname))
  mycursor.execute(message)
  for x in mycursor:
    return x

def deregistration(dogname):
  print("removed account")
  message = ('DELETE FROM Bags WHERE DogName="{dogname}"'.format(dogname=dogname))
  print(message)

  mycursor.execute(message)
  mydb.commit()

showdatabases()
createtable() # is this not needed with update?
showtables()

desc_tables()

# registration('dottie')
# update("dottie")
# new_bags('dottie')
# getRemaingBags('dottie')
# deregistration('dottie')

output()