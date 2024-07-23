#Python'da Donguler Nedir?

#belirli bir kosul veya aralik icinde
#birden fazla kez calismasini saglayan yapidir

#for dongusu ornek1 futbolcu listesi
futbolcu_listesi=["arda","emre","oguz","kubilay","arif"]

for futbolcu in futbolcu_listesi:
    print("Futbolcunun adi:",futbolcu)


for index in range(0,10,1):
    print(index+1)


#while dongusu

sayac=1

while sayac<100:
    print(sayac)
    #sayac = sayac + 2
    sayac +=2

kontrolSayaci=1
while kontrolSayaci < 10:
    if kontrolSayaci == 3 :
        print("dongudeki bu deger atlanacak !")
        kontrolSayaci +=1
        continue
    elif kontrolSayaci == 7 :
        print("dongu burada iptal edildi !")
        break
        
    
    print(kontrolSayaci)
    kontrolSayaci +=1        