import json

data= {'Ad':'Ali','Soyad':'Mavi','Yas':'32'}

with open('dosya.json','w') as file:
    json.dump(data,file)