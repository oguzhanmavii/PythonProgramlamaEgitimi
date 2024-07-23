import os
import glob
from ders10 import dosyayolu
dosyaOku=open(dosyayolu(),"r")
print(dosyaOku.read())

dosyaOku.close()
