from for_nd2_files import main,display_plots
import os
from scipy.optimize import curve_fit
import math
import numpy as np
from matplotlib import pyplot as plt


czasy = [1,2,4,6,8,10,20,40,60,80,              
         100,200,400,600,800,1000,
         2000,4000,6000,8000,10000,
         20000,40000,60000,80000,100000,
         200000,400000,600000]


czasy_ciemnyv2 = [1,10,100,1000]


folder = 'ob20'

pliki = sorted(os.listdir(folder))
if '.DS_Store' in pliki:
    pliki.remove('.DS_Store')
    

seria = 10
ilosc_zdjec = len(pliki)
t = []
for i in range(0,ilosc_zdjec):
    t.append(czasy[i])

ilosc = len(t) * seria


main = main(ilosc,seria,folder,t)

nazwa_zapisanych_plikow = 'ob20'
nazwa_wykresow = 'obiektyw 4'


    
display_plots(main, t, 5,nazwa_zapisanych_plikow,nazwa_zapisanych_plikow)


krok = 2

logt = map(lambda x: math.log2(x/krok),t)
logt = list(logt)

xdata = logt
ydata = main[1]

def sigmoid(x, L ,x0, k, b):
    y = L / (1 + np.exp(-k*(x-x0)))+b
    return (y) 


p0 = [max(ydata), np.median(xdata),1,min(ydata)] 

popt, pcov = curve_fit(sigmoid, xdata, ydata,p0, method='dogbox')

x = np.linspace(-3, 14, 25)
y = sigmoid(x, *popt)

plt.figure(figsize=(15,6))
plt.scatter(y = main[1],x = logt,marker = 'x',color = 'blue')


#zrobic wykres logarytmiczny poszukac w dokumentacji
plt.figure(figsize=(15,6))
plt.scatter(y = main[1],x = logt,marker = 'x',color = 'blue')
plt.plot(x,y ,color = 'red')





model1 = np.poly1d(np.polyfit(xdata, ydata, 1))
plt.figure(figsize=(15,6))
plt.plot(np.log(t),np.log(main[1]),marker = 'x',color = 'red')
plt.plot(np.log(t),np.log(main[2]),marker = 'x',color = 'green')
plt.plot(np.log(t),np.log(main[3]),marker = 'x',color = 'blue')


#co dziesiaty piksel taka chmure
#zgrac wszystkie kanaly zeby otrzymac jak najbardziej podobne obrazy
#metoda najmniejszych kwadratow