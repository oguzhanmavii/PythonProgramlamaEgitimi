import logging

liste = [1,2,3]
try:
    eleman = liste[5]
    print("Liste Elemani:",eleman)
except Exception as e:
    print("Hata: Geçersiz indeks",e)
    
#log ekrana yazdir
logging.basicConfig(level=logging.DEBUG)  

#log dosyaya kaydet
logging.basicConfig(filename='app.log',level=logging.DEBUG)

#log seviyelerine gore ilgili mesajlar 
logging.debug("Bu bir hata ayiklama mesajidir")
logging.info("Bu bir bilgi mesajidir")
logging.warning("Bu bir uyari mesajidir")
logging.error("Bu bir hata mesajidir")
logging.critical("Bu bir kritik hata mesajidir")      