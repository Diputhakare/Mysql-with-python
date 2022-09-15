import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Change@123" )
cursor = mydb.cursor()
s = "insert into dipmala.details values(101 , 'dipmala thakare', 'thakaredipu247@gmail.com' ,10000 , 50)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)

mydb.commit()
cursor.execute("select * from dipmala.details ")
for i in cursor.fetchall():
    print( i)
