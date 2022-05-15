from os import curdir
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

def registration():
  message = """ INSERT INTO Bags(DogName, BagRollAge, InitialBags, Remaining) VALUES ('dottie', 1, 24, 24); """
  mycursor.execute(message)
  mydb.commit()

def update(dogname):
  throw = "SIGNAL"
  print("How many bags used today?")
  bags_used_today = int(input())
  mycursor.execute('SET @Remains := (SELECT Remaining FROM Bags);')
  mycursor.execute('SET @BagsRemaining := ( @Remains - {bags_used_today});'.format(initial_bags=initial_bags,bags_used_today=bags_used_today))
  mycursor.execute(
    """SELECT IF(@BagsRemaining>=1, 'true', 'false');"""
  )
  # turn value into python?
  for x in mycursor:
    print(x)
    if x == ('true',):
      print("bags ok")
    else:
      print("need new bags")
  # throw error
  mycursor.execute('UPDATE Bags SET BagRollAge = 1, Remaining = @BagsRemaining WHERE DogName = "{dogname}";'.format(dogname=dogname))
  mydb.commit()
  

  # remaining = 24 - bags_used_today
  # message = ('UPDATE Bags SET BagRollAge = {bagrollage}, Remaining = {remaining} WHERE DogName = "dottie";'.format(bagrollage=bagrollage,remaining=remaining))
  # mycursor.execute(message)
  # mydb.commit()
  # return bags_used_today

# def getRemaingBags():
#   message = ("Select InitialBagCount FROM Bags;")
#   mycursor.execute(message)
#   for x in mycursor:
#     return x

def deregistration(dogname):
  print("removed account")
  message = ('DELETE FROM Bags WHERE DogName="{dogname}"'.format(dogname=dogname))
  print(message)

  mycursor.execute(message)
  mydb.commit()

# showdatabases()
# createtable()
# showtables()

# desc_tables()

# registration()
update("dottie")
deregistration('dottie')

output()