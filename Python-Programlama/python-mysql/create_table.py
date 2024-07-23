import mysql.connector
connections=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='1234',
    database='persondb'
)

mycursor=connections.cursor()

sql='''create table registation(
    id char(20) not null,
    empname char(20) not null,
    mobile char(20) not null,
    salary char(20) not null,
    INCOME float
)
'''

mycursor.execute(sql)

connections.close()