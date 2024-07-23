import json

with open('dosya.json','r') as file:
    data=json.load(file)
    print(data)