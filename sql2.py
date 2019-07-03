import mysql.connector as db

# ===========================SETUP=========================
mydb=db.connect(\
host="localhost",\
user="newuser",\
passwd="password",\
database="mydatabase")

mycursor=mydb.cursor()
#===========================================================

"""
mycursor.execute("SHOW TABLES;")
for i in mycursor:
        print i
#Table is named  'Test'

mycursor.execute("SELECT * FROM Test;")
myresult=mycursor.fetchall()
for i in myresult:
        print i

+--------+-----------+----------+
| userid | username  | password |
+--------+-----------+----------+
"""
#===============================================================

usr=int(input("Enter user id : "))
name=raw_input("Enter username : ")
type(name)
passwd=raw_input("Enter password : ")
type(passwd)

#===================STORING IN DATABASE=========================
"""val=(int(usr),name,passwd)
mycursor.execute("INSERT INTO Test VALUES (%s,'%s','%s')"%(val))
mydb.commit()
print  mycursor.rowcount, "record inserted."
"""

mycursor.execute("SELECT * FROM Test;")
myresult=mycursor.fetchall()
for i in myresult:
        usr,name,passwd=i
        print usr,
        print '%3s'%'| ',
        print name,
        print'%1s'%'| ',
        print passwd



