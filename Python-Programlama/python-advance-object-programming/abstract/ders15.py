from dikdortgen import Dikdortgen
from kare import Kare
from ucgen import Ucgen

print("Dikdortgenin Alani")
dikdortgen=Dikdortgen(8,11)
sonuc=dikdortgen.alan_hesaplama()
print(sonuc)

print("Karenin Alani")
kare=Kare(5)
sonuc=kare.alan_hesaplama()
print(sonuc)

print("Ucgenin Alani")
ucgen=Ucgen(12,18)
sonuc=ucgen.alan_hesaplama()
print(sonuc)