import random

def kare_al(sayi):
    sonuc=sayi ** 2
    print("Karesi alinan sayi",sonuc)


def mod_al(sayi,mod):
    sonuc=sayi % mod
    print("Mod:",sonuc)    
    


def cift_sayilari_al(baslangic,bitis):
    for bul in range(baslangic,bitis):
        if bul % 2 == 0:
            print("Bu bir cift sayidir:",bul)
        else:
            continue
        
        
def sansli_sayi(baslangic,bitis):
    sonuc=random.randrange(baslangic,bitis)
    print("Sansli Sayi:",sonuc)
                