import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Change@123" )
cursor = mydb.cursor()
cursor.execute("create database dipmala")
# first run  create database after that run create table
s = "create table dipmala.details(employe_id int(10)  , emp_name varchar(80) , emp_mailid varchar(20),emp_salary int(6) , emp_attendence int(3))"
q1 = cursor.execute(s)

q2 = cursor.execute("select * from dipmala.details")
print(q2)


