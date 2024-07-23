import sqlite3

#veritabani baglantisi kuralim
connection=sqlite3.connect('veritabani.db')

#bir cursor olusturalim
cursor=connection.cursor()

#db'de tablo olusturalim
cursor.execute('''
        CREATE TABLE IF NOT EXISTS tablo(
                   s1 TEXT,
                   s2 TEXT,
                   s3 TEXT,
                   s4 TEXT, 
                   s5 TEXT
               )
''')
#veritabani baglantisini kaydedelim (commit)
connection.commit()

#sql sorugusunu db'deki tablo adli tabloya ekleyelim
cursor.execute('INSERT INTO tablo (s1,s2,s3,s4,s5) VALUES(?,?,?,?,?)',
               ('Python Eğitimi','Java Eğitimi','Flutter Mobil Programlama Eğitimi',
                'C# Eğitimi','Linux Eğitimi'))

#veritabani baglantisini kaydedelim
connection.commit()


#veritabanini kapatmaliyiz
connection.close()