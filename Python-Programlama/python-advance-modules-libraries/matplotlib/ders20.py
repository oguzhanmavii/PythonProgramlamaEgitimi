import matplotlib.pyplot as plt 
import numpy as np

#Ornek veriler olusturalim
x= np.linspace(0,10,100)
y1= np.sin(x)
y2= np.cos(x)


#iki farkli grafigi cizdirelim
plt.plot(x,y1, label='sin(x)')
plt.plot(x,y2, label='cos(x)')

#Eksen etiketlerini olusturalim
plt.xlabel('x ekseni')
plt.ylabel('y ekseni')
plt.title('Sin(x) ve Cos(x) Grafikleri')

#Grafik aciklamalari
plt.legend()

#Grafigimizin cizimini tamamlayali
plt.show()