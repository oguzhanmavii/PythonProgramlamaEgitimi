from ITasit import *
import time
class Araba(TasitAraciArayuzu):
    def hareket_et(self):
        time.sleep(1.6)
        print("araba motoru calistiriliyor..")
    
    
    def hizlan(self):
        time.sleep(1.6)
        print("Araba vitesi arttirildi araba hizlaniyor..")
        
    
    def yavasla(self):
        time.sleep(1.6)
        print("Araba vitesi dusuruldu araba yavasliyor..")
    
    
    def dur(self):
        time.sleep(1.6)
        print("Araba durdu !")       