#Python'da Diziler ve Liste Islemleri Nedir?

#diziler farkli veri türlerini icerebilen ve sirali bir sekilde tutulan
#veri koleksiyonlaridir

#dizi & liste olusturma
arabaListesi=["Bmw","Audi","Kia","Ford","Wolkswagen","Toyata","Fiat","Hyundai"]
karmasikListe=[7,"Python Programlama",3.14,False]

#dizi elamanlarina erisim
sonuc=arabaListesi[7]
print(sonuc)

sonuc2=karmasikListe[0]
print(sonuc2)

#dizi dilimleme
subset=arabaListesi[1:5]
print(subset)

#diziye eleman ekleme
karmasikListe.append(True)

#dizi uzunlugu
uzunluk=len(karmasikListe)
print(uzunluk)

#diziden eleman cikarma
karmasikListe.pop(3) # index'i 3 olan eleman listeden silinir


#dizi birlestirme
birlestirilmisListe=arabaListesi + karmasikListe
print(birlestirilmisListe)


#dizi elemanlarini sirala
sayisal_degerler=[eleman for eleman in birlestirilmisListe if isinstance(eleman,(int,float))]
metinsel_degerler=[eleman for eleman in birlestirilmisListe if isinstance(eleman,str)]
sayisal_degerler.sort()
metinsel_degerler.sort()
print(sayisal_degerler,metinsel_degerler)

#dizi icinde eleman kontrolu
if 9 in birlestirilmisListe:
    print("9 elemani listede var")
else:
    print("9 elemani listede yok")


#diziyi eleman eleman gostermek istiyorsak
for eleman in birlestirilmisListe:
    print(eleman)
    

#dizi kopyalama islemi
#yeni_kopya=karmasikListe[:]
yeni_kopya=karmasikListe.copy()
print(yeni_kopya)


#ic ice dizi olusturmak
matrix=[[1,2,3],[4,5,6],[7,8,9]]   
for matrix in matrix:
    print(matrix)
    