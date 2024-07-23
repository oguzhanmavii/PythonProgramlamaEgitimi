from base import Sekil

class Kare(Sekil):
    def __init__(self,kenar):
        self.kenar=kenar
        
    def alan_hesaplama(self):
        return self.kenar ** 2  