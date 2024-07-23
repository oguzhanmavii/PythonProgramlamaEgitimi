import pandas as pd
#Bir DataFrame oluşturalim

data={
    'Öğrenci':['Ali','Ayşe','Mehmet','Zeynep','Ahmet'],
    'Not':[85,90,78,92,88],
    'Sınıf':[10,11,10,12,11]
}

df=pd.DataFrame(data)
#DataFrame'i ekrana yazdırın
print("Ogrenci Bilgileri:")
print(df)
#sadece belirli bir sutunu secin ve siralayin
sorted_df=df[['Öğrenci','Not']].sort_values(by='Not',ascending=False)
#siralanmis DataFrame'i ekranda gosterelim
print("\nNotlara Gore Siralanmis Ogrenci Bilgileri:")
print(sorted_df)