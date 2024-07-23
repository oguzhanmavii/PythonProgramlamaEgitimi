import mysql.connector


mydatabase=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1234'
)

mycursor=mydatabase.cursor()
mycursor.execute('show databases')

print('-----Mysql Veritabanimdaki Veritabanlarim-----')

for databases in mycursor:
    print(databases)