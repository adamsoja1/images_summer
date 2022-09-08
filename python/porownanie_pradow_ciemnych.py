#069 i 074, 079,084,089  seria 3 ciemny

import nd2
from matplotlib import pyplot as plt
import numpy as np
import os
import math

from for_nd2_files import main,display_plots

folder = 'ciemny v 2'
folder2 = 'zdjcia2'

#1 10 100 1000 dla czas pracy

pliki1 = sorted(os.listdir(folder))
pliki2 = sorted(os.listdir(folder2))

if '.DS_Store' in pliki1:
    pliki1.remove('.DS_Store')
    
if '.DS_Store' in pliki2:
    pliki2.remove('.DS_Store')

t= [1,10,100,1000,10000]
seria = 10
ilosc = len(t) * seria

main1 = main(ilosc,seria,folder,t)

main2 = main(ilosc,seria,folder2,t)

krok = 2
logt = map(lambda x: math.log2(x/krok),t)
logt = list(logt)




plt.figure(figsize=(15,11))
plt.title('Kanał B dla centrum obrazu porownanie')
plt.scatter(y =main1[3] ,x = logt,marker = 'x',color = 'red')
plt.scatter(y = main2[3],x = logt,marker = 'x',color = 'green')
plt.ylabel('Wartość piksela')
plt.xlabel('log2(t/t0)')
    

plt.figure(figsize=(15,11))
plt.title('Kanał G dla centrum obrazu porownanie')
plt.scatter(y =main1[2] ,x = logt,marker = 'x',color = 'red')
plt.scatter(y = main2[2],x = logt,marker = 'x',color = 'green')
plt.ylabel('Wartość piksela')
plt.xlabel('log2(t/t0)')
    
plt.figure(figsize=(15,11))
plt.title('Kanał R dla centrum obrazu porownanie')
plt.scatter(y =main1[1] ,x = logt,marker = 'x',color = 'red')
plt.scatter(y = main2[1],x = logt,marker = 'x',color = 'green')
plt.ylabel('Wartość piksela')
plt.xlabel('log2(t/t0)')
    





display_plots(main1, t, 5,'ciemny 0','ciemny 0')
display_plots(main2, t, 5,'ciemny 30min','ciemny 30min')







