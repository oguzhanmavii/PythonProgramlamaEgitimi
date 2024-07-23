#Python'da Veri Türleri Nedir ?

'''
Sayisal Veri Türleri:
int: Tam Sayilari temsil eder ornek: 42 
float:Ondalikli Sayilari temsil eder ornek: 2.78
complex:Karmasik Sayilari temsil eder ornek: 2 + 3j

Metinsel Veri Türleri:
str: Metin ve Karakter dizinlerini temsil eder. ornek: 'Merhaba Dünya !'


Mantiksal Veri Türleri:
bool: Mantiksal degerleri temsil eder Sadece True veya False tipinde tanimlanir


Kolesksiyon Veri Türleri:
list:Sirali,degistirilebilir elamanlar iceren bir koleksiyondur Ornek:[1,2,3]
tuple:Sirali,degistirilemez elemanlar iceren bir koleksiyondur  Ornek:(1,2,3)
set:Benzersiz elemanlar icerin bir koleksiyondur Ornek:{1,2,3}
dict:Anahtar-deger ciftleri iceren bir koleksiyondur Ornek:{'ad':'oguzhan'}


Dizi Veri Turu:

array: Numpy kutuphanesi ile kullanilan homojen veri dizileridir.

NoneType: Herhangi bir degeri olmayan genellikle bir bosluk veya tanimsizlik
durumunu temsil eder Ornek:None


'''

komplex_sayi=2+3j
print(komplex_sayi)

reel_kisim=komplex_sayi.real
print("Reel Kisim:",reel_kisim)

imaginer_kisim=komplex_sayi.imag
print("Imaginer Kisim:",imaginer_kisim)