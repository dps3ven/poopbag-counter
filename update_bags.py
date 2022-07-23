import mysql.connector
import os

## sourced from environment
print("What is your dog's name?")
dogname = str(input())
initial_bags = 24
mydb = mysql.connector.connect(
  host=(os.environ["database_host"]),
  user=(os.environ["database_user"]),
  password=(os.environ["database_user_password"])
)
mydb.database=(os.environ["database_name"])
mycursor = mydb.cursor()
print("How many bags used today?")
bags_used_today = int(input())
try:
    q='SET @BagsRemaining := ( @Remains - {bags_used_today});'.format(initial_bags=initial_bags,bags_used_today=bags_used_today)
    mycursor.execute('SET @Remains := (SELECT Remaining FROM Bags WHERE DogName = "{dogname}");'.format(dogname=dogname))
    mydb.commit()
    mycursor.execute(q)
    mydb.commit()
    x='SELECT Remaining from Bags WHERE DogName = "{dogname}";'.format(dogname=dogname)
    mycursor.execute(x)
    bags_left = mycursor.fetchone()[0]
except:
    print("Registation Error")
    raise Exception("Verify Registration for {}".format(dogname))
bags_left = bags_left - bags_used_today ## lazy and should be put into separate function
print(bags_left)
if bags_left >=2:
    mycursor.execute('UPDATE Bags SET Remaining = @BagsRemaining WHERE DogName = "{dogname}";'.format(dogname=dogname))
    mydb.commit()
elif bags_left ==1:
    print("Warning: New Bag Roll Needed")
    mycursor.execute('UPDATE Bags SET Remaining = @BagsRemaining WHERE DogName = "{dogname}";'.format(dogname=dogname))
    mydb.commit()
    raise Exception("One Bag Left - Warning You") 
else:
    x='UPDATE Bags SET Remaining = 0 WHERE DogName = "{dogname}";'.format(dogname=dogname)
    mycursor.execute(x)
    mydb.commit()
    raise Exception("No More Bags Left") 

