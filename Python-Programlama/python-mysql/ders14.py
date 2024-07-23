import mysql.connector
import time

hostname=input('hostname  giriniz:')
username=input('username  giriniz:')
password=input('password  giriniz:')
database=input('database  giriniz:')
mydatabese=mysql.connector.connect(
    host=hostname,
    user=username,
    password=password,
    database=database,
)
print('database baglantisi gerçekleştiriliyor..')
time.sleep(3)
print('database başarili şekilde bağlanildi !')

mydatabese.close()