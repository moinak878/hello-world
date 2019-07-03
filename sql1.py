#CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
#GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';


import mysql.connector as db
#mydb=db.connect(host="localhost",user='newuser',passwd='password')

#print mydb

#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
"""
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
"""

mydb = db.connect(
  host="localhost",
  user="newuser",
  passwd="password",
  database="mydatabase"
)
mycursor=mydb.cursor()

#mycursor.execute("CREATE TABLE Test (userid integer PRIMARY KEY , username varchar(20) NOT NULL , password varchar(8))")

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

