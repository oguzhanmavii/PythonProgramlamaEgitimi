from ITasit import *
import time
class Bisiklet(TasitAraciArayuzu):
    def hareket_et(self):
        time.sleep(1.6)
        print("Pedallar çeviriliyor..")
    
    
    def hizlan(self):
        time.sleep(1.6)
        print("Bisiklet vitesi arttirildi Bisiklet hizlaniyor..")
    
    
    def yavasla(self):
        time.sleep(1.6)
        print("Bisiklet vitesi dusuruldu Bisiklet yavasliyor..")
    
    
    def dur(self):
        time.sleep(1.6)
        print("Bisiklet durdu !")       