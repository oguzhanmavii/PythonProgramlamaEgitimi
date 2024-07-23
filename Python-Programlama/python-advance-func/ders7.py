#Python'da ileri seviye fonksiyonlar nelerdir?(args kwargs lambda fonksiyonlari)

#*args ve **kwargs
#bu iki ozel parametre fonksiyonlara degisken sayida argumanlari gecmenizi saglarlar.

#1.) *args

def total(*args):
    sonuc=0
    for arg in args:
        sonuc = sonuc + arg
    return sonuc


print(total(1,2,3,4,5))


#2.) **kwargs

def information(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
        

information(firstname="Oguzhan",lastname="Mavi",yas=24,meslek="Yazilim muhendisi")




#3-) lambda fonksiyonlari
#lambda fonksiyonlari isimsiz islevleri tanimlamak icin kullanilir
#genellikle kisa ve tek seferlik kullanimlarda tercih edilir 

kup_al=lambda x: x ** 3
print("Lambda Fonksiyonu Kup Hesaplama Sonucu:",kup_al(5))


number_list=[1,3,5,7,9,12,4,6,8,2,10,11,19]
#lamda'da listeleme yapacagiz

n4=list(map(lambda x : x **4 ,number_list))
print("Number List:",n4)


#lambda listelemede filtreleme mantigi
number_filter=list(filter(lambda x : x % 2 == 0,number_list))
print("Number Filter:",number_filter)
   
   
#lambda ile kucukten buyuge liste siralama mantigi
number_sort=list(sorted(number_list,key=lambda x : x))
print("Number Sorted:",number_sort)

#lambda ile  buyukten kucuge liste siralama mantigi
number_sort=list(sorted(number_list,key=lambda x : -x))
print("Number Sorted:",number_sort)      