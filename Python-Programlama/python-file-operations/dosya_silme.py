import os 
import glob
from ders10 import dosyayolu

if os.path.exists(dosyayolu()):
    os.remove(dosyayolu())

else:
    print("Böyle bir dosya bulunamadi !")    