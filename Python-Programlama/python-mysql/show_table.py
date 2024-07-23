import mysql.connector

mydatabase=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1234',
    database='persondb'
)

mycursor=mydatabase.cursor()
mycursor.execute('show tables')


print('-----persondb içerisindeki tablolarimiz-----')

for tables in mycursor:
    print(tables)