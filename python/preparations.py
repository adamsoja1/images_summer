import nd2
from matplotlib import pyplot as plt
import numpy as np
from for_nd2_files import srednia, srednia_kat_lewyDolny,srednia_kat_lewyGorny
import os
from for_nd2_files import srednia_kat_prawyDolny,srednia_kat_prawyGorny
folder = 'nadnercza'

pliki = sorted(os.listdir(folder))
if '.DS_Store' in pliki:
    pliki.remove('.DS_Store')
    
srednia_centrum = []
srednia_kata_prawyGorny = []
srednia_kata_prawyDolny= []
srednia_kata_lewyGorny= []
srednia_kata_lewyDolny = []


y=[]
for i in range(len(pliki)):
    obraz = nd2.imread(f'{folder}/{pliki[i]}')
    for j in range(0,len(obraz)):
        ob = obraz[j]
        srednia_centrum.append(srednia(ob))
        srednia_kata_prawyGorny.append(srednia_kat_prawyGorny(ob))
        srednia_kata_prawyDolny.append(srednia_kat_prawyDolny(ob))
        srednia_kata_lewyGorny.append(srednia_kat_lewyGorny(ob))
        srednia_kata_lewyDolny.append(srednia_kat_lewyDolny(ob))
    nazwa = pliki[i]
    y.append(nazwa[4:7])


temp = np.array(srednia_centrum)
centrum_r = np.array(temp[:,0])
centrum_g = np.array(temp[:,1])
centrum_b = np.array(temp[:,2])


centrum_r1 = []
centrum_g1 = []
centrum_b1 = []

kat_r1_prawyGorny = []
kat_g1_prawyGorny = []
kat_b1_prawyGorny = []

kat_r1_prawyDolny = []
kat_g1_prawyDolny = []
kat_b1_prawyDolny = []

kat_r1_lewyDolny = []
kat_g1_lewyDolny = []
kat_b1_lewyDolny = []

kat_r1_lewyGorny = []
kat_g1_lewyGorny = []
kat_b1_lewyGorny = []




temp2_prawyGorny = np.array(srednia_kata_prawyGorny)
temp2_prawyDolny = np.array(srednia_kata_prawyDolny)
temp2_lewyGorny = np.array(srednia_kata_lewyGorny)
temp2_lewyDolny = np.array(srednia_kata_lewyDolny)

kat_r_prawyGorny = np.array(temp2_prawyGorny[:,0])
kat_g_prawyGorny = np.array(temp2_prawyGorny[:,1])
kat_b_prawyGorny = np.array(temp2_prawyGorny[:,2])

kat_r_prawyDolny = np.array(temp2_prawyDolny[:,0])
kat_g_prawyDolny = np.array(temp2_prawyDolny[:,1])
kat_b_prawyDolny = np.array(temp2_prawyDolny[:,2])

kat_r_lewyDolny = np.array(temp2_lewyDolny[:,0])
kat_g_lewyDolny = np.array(temp2_lewyDolny[:,1])
kat_b_lewyDolny = np.array(temp2_lewyDolny[:,2])

kat_r_lewyGorny = np.array(temp2_lewyGorny[:,0])
kat_g_lewyGorny = np.array(temp2_lewyGorny[:,1])
kat_b_lewyGorny = np.array(temp2_lewyGorny[:,2])



seria = len(obraz) - 1
licznik = 0
for i in range(0,len(pliki)):
    
    centrum_r1.append(np.mean(centrum_r[licznik:licznik+j]))
    centrum_g1.append(np.mean(centrum_g[licznik:licznik+j]))
    centrum_b1.append(np.mean(centrum_b[licznik:licznik+j]))

    kat_r1_prawyGorny.append(np.mean(kat_r_prawyGorny[licznik:licznik+j]))
    kat_g1_prawyGorny.append(np.mean(kat_g_prawyGorny[licznik:licznik+j]))
    kat_b1_prawyGorny.append(np.mean(kat_b_prawyGorny[licznik:licznik+j]))
    
    
    kat_r1_prawyDolny.append(np.mean(kat_r_prawyDolny[licznik:licznik+j]))
    kat_g1_prawyDolny.append(np.mean(kat_g_prawyDolny[licznik:licznik+j]))
    kat_b1_prawyDolny.append(np.mean(kat_b_prawyDolny[licznik:licznik+j]))
    
    kat_r1_lewyDolny.append(np.mean(kat_r_lewyDolny[licznik:licznik+j]))
    kat_g1_lewyDolny.append(np.mean(kat_g_lewyDolny[licznik:licznik+j]))
    kat_b1_lewyDolny.append(np.mean(kat_b_lewyDolny[licznik:licznik+j]))
    
    kat_r1_lewyGorny.append(np.mean(kat_r_lewyGorny[licznik:licznik+j]))
    kat_g1_lewyGorny.append(np.mean(kat_g_lewyGorny[licznik:licznik+j]))
    kat_b1_lewyGorny.append(np.mean(kat_b_lewyGorny[licznik:licznik+j]))
   
    
    
    
    licznik = licznik + seria
    
    
    
    
#%%    
plt.figure(figsize=(45,10))
plt.title('Kanały RGB dla centrum obrazu ')
plt.scatter(y =centrum_r1 ,x = pliki,marker = 'x',color = 'red')
plt.scatter(y = centrum_g1,x = pliki,marker = 'x',color = 'green')
plt.scatter(y = centrum_b1,x = pliki,marker = 'x',color = 'blue')
plt.ylabel('Wartość piksela')
plt.xlabel('Numer obrazu')
plt.savefig('plots/segments1_centrum.png')


plt.figure(figsize=(45,10))
plt.title('Kanały RGB dla prawy gorny obrazu ')
plt.scatter(y = kat_r1_prawyGorny ,x = pliki,marker = 'x',color = 'red')
plt.scatter(y = kat_g1_prawyGorny,x = pliki,marker = 'x',color = 'green')
plt.scatter(y = kat_b1_prawyGorny,x = pliki,marker = 'x',color = 'blue')
plt.ylabel('Wartość piksela')
plt.xlabel('Numer obrazu')
plt.savefig('plots/segments1_prawygorny.png')


plt.figure(figsize=(45,10))
plt.title('Kanały RGB dla lewy dolny obrazu ')
plt.scatter(y = kat_r1_lewyDolny ,x = pliki,marker = 'x',color = 'red')
plt.scatter(y = kat_g1_lewyDolny,x = pliki,marker = 'x',color = 'green')
plt.scatter(y = kat_b1_lewyDolny,x = pliki,marker = 'x',color = 'blue')
plt.ylabel('Wartość piksela')
plt.xlabel('Numer obrazu')
plt.savefig('plots/segments1_lewydolny.png')



plt.figure(figsize=(45,10))
plt.title('Kanały RGB dla prawy dolny obrazu ')
plt.scatter(y = kat_r1_prawyDolny ,x = pliki,marker = 'x',color = 'red')
plt.scatter(y = kat_g1_prawyDolny,x = pliki,marker = 'x',color = 'green')
plt.scatter(y = kat_b1_prawyDolny,x = pliki,marker = 'x',color = 'blue')
plt.ylabel('Wartość piksela')
plt.xlabel('Numer obrazu')
plt.savefig('plots/segments1_prawydolny.png')



plt.figure(figsize=(45,10))
plt.title('Kanały RGB dla lewy dolny obrazu ')
plt.scatter(y = kat_r1_lewyGorny ,x = pliki,marker = 'x',color = 'red')
plt.scatter(y = kat_g1_lewyGorny,x = pliki,marker = 'x',color = 'green')
plt.scatter(y = kat_b1_lewyGorny,x = pliki,marker = 'x',color = 'blue')
plt.ylabel('Wartość piksela')
plt.xlabel('Numer obrazu')
plt.savefig('plots/segments1_lewygorny.png')
