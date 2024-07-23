import csv


data= [
    ['Ad','Soyad','Yas'],
    ['Ahmet','Yılmaz','25'],
    ['Ayse','Demir',30]
]

with open('dosya.csv','w', newline='') as file:
    csv_writer= csv.writer(file)
    csv_writer.writerows(data)