import mysql.connector
import time
import sys

mydb = mysql.connector.connect(
  host="192.168.1.27",
  user="root",
  password="admin",
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS poopbags") ## var

mydb.database = "poopbags" ## var this is use database


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

## two functions
# #### registration
def registration():
  mycursor.execute("INSERT INTO Bags VALUES('dottie',1,25);")
# ## one for updates

    # # prepare query and data
    # query = """ UPDATE books
    #             SET title = %s
    #             WHERE id = %s """

    # data = (title, book_id)

    # try:
    #     conn = MySQLConnection(**db_config)

    #     # update book title
    #     cursor = conn.cursor()
    #     cursor.execute(query, data)


# update_format = """UPDATE Bags SET BagRollAge = 2, Remaining = %d WHERE DogName = 'dottie'""", sys.argv[1]

def update(num):
  print(num)
  update = ('Hello %s! This is %s.'%(num,num))

  txt = (("UPDATE Bags SET BagRollAge = %s, Remaining = 22 WHERE DogName = 'dottie';"%num))
  print('Hello %s! This is %s.'%(num,num))
  print(txt)
  # print(txt.format("UPDATE Bags SET BagRollAge = 2, Remaining = num WHERE DogName = 'dottie';")) 
  mycursor.execute(txt)
  # for x in mycursor:
  #   print(x)
  
  # int = int
  # query = """ 
  # #   UPDATE Bags
  # #   SET Remaining = num
  # #   WHERE DogName = dottie 
  # """
  # txt = "For only {price:.2f} dollars!"

  # mycursor.execute(query, [44])
  # for x in mycursor:
  #   print(x)

def output():
  mycursor.execute("Select * FROM Bags;")
  for x in mycursor:
    print(x)

def showdatabases():
  mycursor.execute("SHOW DATABASES")
  for x in mycursor:
    print(x) 

def createtable():
  mycursor.execute("CREATE TABLE IF NOT EXISTS Bags (DogName varchar(255) NOT NULL PRIMARY KEY, BagRollAge int, Remaining int)") ## OWNER IS PRIMARY KEY?


showdatabases()
createtable()

registration()
showtables()


update(666)
output()
