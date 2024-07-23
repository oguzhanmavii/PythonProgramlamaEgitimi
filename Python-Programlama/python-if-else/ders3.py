#Python'da Kosullu ifadeler ve Karar yapilari Nedir?

#Programlarimizin belirli şartlara gore 
#farklı davranışlar reaksiyonlar sergilemesini saglayan yapidir

#ornek1 ogrencinotu 50'den dusukse ogrenci dersten kalicak

sinavPuani=int(input("Notunuzu giriniz:"))

if sinavPuani<50:
    print("Dersten Kaldiniz !")

else:
    print("Tebrikler Dersi Gectiniz")
    

#ornek2 hava sicakligi olcme
#sicaklik -10 ve 10 derece arasinda ise hava soguk
#sicaklil 10 ve 20 derece arasinda ise  hava normal
#sicaklik 20 ve 50 derece arasinda ise  hava sicak



havaSicakligi=int(input("Bugunki Hava Sicakligini giriniz:"))

if havaSicakligi>=-10 and havaSicakligi <10:
    print("Bugun hava soguk")

elif havaSicakligi>=10 and havaSicakligi <=20:
    print("Bugun hava normal")

elif havaSicakligi>20 and havaSicakligi<=50:
    print("Bugun hava sicak")

else:
    print("Hava sicakligi olculemedi !")            
             