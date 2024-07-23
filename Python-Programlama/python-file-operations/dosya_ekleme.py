import os 
from ders10 import dosyayolu

dosyaEkle=open(dosyayolu(),"a")
with open(dosyayolu(),"a") as dosya:
    veri=input("Birseyler yaz:")
    dosya.write(veri+"\n")
dosyaEkle.close()    