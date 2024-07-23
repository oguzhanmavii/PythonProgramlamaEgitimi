from base import Sekil

class Ucgen(Sekil):
    def __init__(self,taban,yukseklik):
        self.taban=taban
        self.yukseklik=yukseklik
        
    def alan_hesaplama(self):
        return (self.taban * self.yukseklik) / 2 