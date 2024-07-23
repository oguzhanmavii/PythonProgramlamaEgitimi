import mysql.connector

mydatabase=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1234'
)

mycursor=mydatabase.cursor()
mycursor.execute('create database persondb')