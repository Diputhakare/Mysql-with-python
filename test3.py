import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Change@123" )
cursor = mydb.cursor()
cursor.execute("select employe_id , emp_mailid from dipmala.details")
l = []
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))