from base import Sekil

class Dikdortgen(Sekil):
    def __init__(self,kisakenar,uzunkenar):
        self.kisakenar=kisakenar
        self.uzunkenar=uzunkenar
    
    def alan_hesaplama(self):
        return (self.kisakenar + self.uzunkenar) * 2
        
        