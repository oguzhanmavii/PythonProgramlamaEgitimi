#python'da hata yakalama ve istisna yonetimi
#try ve except sayesinde programınız çalışırken
#oluşabilecek hataları yakalayabilir istisnaya özel işlemler
#gerçekleştirebilirsiniz.

#ornek 1

try:
     sayi=int(input("Bir sayi giriniz:"))
     sonuc=10/sayi
     print("Sonuc:",sonuc)

except ZeroDivisionError:
     print("Hata:",'Bir sayi 0 a bolunemez !')
     
except ValueError:
    print("Hata:","Gecerli bir sayi girmediniz !")

except Exception as exception:
    print("Beklenmeyen bir hata olustu !",exception)         


except KeyboardInterrupt as key:
    print("Klavyeden dogru degerleri girmediniz ",key)

finally:
     print("Islem tamamlandi !")        
    