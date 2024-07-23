#Python'da modüller ve kütüphaneler kodunuzu genişletmek
#işlevselliği artirmak için kullanilan önemli terimlerdir

#Modül Nedir ?
#Bir Python dosyasidir (genellikle .py uzantili).
#İşlevleri, siniflari veya değişkenleri içerebilir.
#Başka Python dosyalarinda kullanilabilir.
#import anahtar kelimesi ile içe aktarilir.

def hello():
    print("Hello, Python!")
    
#baska bir dosya veya modülde içeri aktarmak için şu şekilde kullanilir
import ders13
ders13.hello()

#Kütüphane Library Nedir ?
#Modüllerin ve fonksiyonların koleksiyonudur.
#belirli bir amaç için bir araya getirilmiş modüllerden oluşur.
#Python, çok sayıda standart kütüphane ile birlikte gelir
#kütüphaneler geniş bir işlevselliği kapsar.

import datetime
bugun=datetime.date.today()
print(bugun)

#math kütüphanesinden bir işlevi kullanalim
import math
derece=45
radyan=math.radians(derece)
print(f"{derece} derece, {radyan} radyandir")

#Üçüncü taraf kütüphaneleri
#Bu kütüphaneler, pip veya conda gibi paket yöneticileri ile yüklenir.

# Üçüncü taraf bir kütüphaneyi içe aktarma
import numpy as np

sayi=np.random.rand(1,10)
print(sayi) 

#Birazda Sistem Modüllerinden bahsedelim
import os

#Geçerli çalışma dizini
print(os.getcwd())
# Dizindeki dosyaları listeleme
print(os.listdir())

#os.mkdir("yeni_dizin")

#os.rmdir("yeni_dizin")

import sys
#komut satiri argümanlarini alma
print(sys.argv) 