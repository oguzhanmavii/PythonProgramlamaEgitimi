def aort_dekorator(fonksiyon):
    def wrapper(*args):
        sonuc=fonksiyon(*args)
        ortalama= sum(args) / len(args)
        print(f"{fonksiyon.__name__} işleminin aritmetik ortalamasi:{ortalama}")
        return sonuc
    return wrapper


@aort_dekorator
def toplama(*sayilar):
    return sum(sayilar)

aritmetik_ortalama_sonucu=toplama(2,4,6,8,10)


@aort_dekorator
def carpma(*sayilar):
    sonuc=1
    for sayi in sayilar:
        sonuc *= sayi
    return sonuc

aritmetik_carpma_sonucu=carpma(1,3,5,7)    