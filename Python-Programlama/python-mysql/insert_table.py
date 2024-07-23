import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="1234",
    database="persondb"
)

mycursor = mydb.cursor()

sql = "insert into customer(id,custname,mobile,salary) VALUES (%s,%s,%s,%s)"
val = ("1", "Oguzhan Mavi","5425169336","100000")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")