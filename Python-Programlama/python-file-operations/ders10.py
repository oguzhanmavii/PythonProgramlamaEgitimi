#file handling

#Dosya Yönetemi
#Pythonda dosyalarla çalışmanın temel işlevi open()'dır

#Fonksiyon open() iki parametre alır dosya adı ve mod

#bir dosyayı açmak için dört farklı yöntem mod vardır

#"r"- Oku Varsayılan deger Okumak için bir dosya açar dosya yoksa hata verir

#"a"- Ekle Eklemek üzere bir dosya açar mevcut değilse dosyayı oluşturur

#"w"- Yaz Yazmak için bir dosya açar yoksa dosyayı oluşturur 

#"x"- Oluştur Belirtilen dosyayı oluşturur dosya varsa hata verir

#Ek olarak dosyanın ikili veya metin modu olarak mı ele alınması gerektigini
#belirleyebilirsiniz

#"t"- Metin Varsayılan değer Metin Modu

#"b"- İkili Mod (Örneğin Resimler)

import os   #dosya okuma işlemleri için kullanılan kütüphane import edilmesi gerekir
import glob #dosyaları isimlerini kullanabilmek için glob import edilir

def dosyayolu():
    return 'C://Users//oguzh//Python-Programlama//python-file-operations//dosya.txt'