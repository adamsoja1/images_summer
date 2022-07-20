from matplotlib import pyplot as plt
import cv2
import numpy as np
from PIL import Image
import seaborn as sns
import math


def srednia(img):
    x = np.shape(img)[0]
    y = np.shape(img)[1]
    
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]
    
    cent1 = int(round(x/2))
    cent2 = int(round(y/2))
    
    box_r1 = red[cent1-50:cent1+50,cent2-50:cent2+50]
    box_g2= green[cent1-50:cent1+50,cent2-50:cent2+50]
    box_b3 = blue[cent1-50:cent1+50,cent2-50:cent2+50]
    
    box_r = np.mean(box_r1)
    box_g = np.mean(box_g2)
    box_b = np.mean(box_b3)
    
    arr = [box_r,box_g,box_b]
    return arr


def srednia_kat(img):
    
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]
    
    box_r = red[1:100,1:100]
    box_g = green[1:100,1:100]
    box_b = blue[1:100,1:100]
    
    s1 = np.mean(box_r)
    s2 = np.mean(box_g)
    s3 = np.mean(box_b)
    arr = [s1,s2,s3]
    return np.array(arr)
    





def main(numer,ilosc,seria,sciezka,t):
    
    iteracje = [i for i in range(1,ilosc+1)]
    
    srednia_centrum = []
    srednia_kata = []
    


    

    for i in range(0,ilosc):
        wartosc = numer + i
        obraz = plt.imread(f'{sciezka}/IMG00{wartosc}.JPG')
        srednia_centrum.append(srednia(obraz))
    
        srednia_kata.append(srednia_kat(obraz))
        
    
    temp = np.array(srednia_centrum)
    temp2 = np.array(srednia_kata)
    centrum_r = np.array(temp[:,0])
    centrum_g = np.array(temp[:,1])
    centrum_b = np.array(temp[:,2])
    
    
    
    
    plt.figure(figsize=(15,6))
    plt.scatter(y = centrum_r,x = iteracje,marker = '.',color = 'red')
    plt.scatter(y = centrum_g,x = iteracje,marker = '.',color = 'green')
    plt.scatter(y = centrum_b,x = iteracje,marker = '.',color = 'blue')
    kat_r = np.array(temp2[:,0])
    kat_g = np.array(temp2[:,1])
    kat_b = np.array(temp2[:,2])
    
    plt.figure(figsize=(15,6))
    plt.scatter(y = kat_r,x = iteracje,marker = '.',color = 'red')
    plt.scatter(y = kat_g,x = iteracje,marker = '.',color = 'green')
    plt.scatter(y = kat_b,x = iteracje,marker = '.',color = 'blue')
    plt.title('Kat')
    
    
    centrum_r1 = []
    centrum_g1 = []
    centrum_b1 = []
    
    kat_r1 = []
    kat_g1 = []
    kat_b1 = []

    
    srednia_centrum = np.array(srednia_centrum)
    
    
    j = seria - 1
    licznik = 0
    
    for i in range(0,len(t)):
        centrum_r1.append(np.mean(centrum_r[licznik:licznik+j]))
        centrum_g1.append(np.mean(centrum_g[licznik:licznik+j]))
        centrum_b1.append(np.mean(centrum_b[licznik:licznik+j]))
        kat_r1.append(np.mean(kat_r[licznik:licznik+j]))
        kat_g1.append(np.mean(kat_g[licznik:licznik+j]))
        kat_b1.append(np.mean(kat_b[licznik:licznik+j]))
        licznik = licznik + seria 
        
        
    return srednia_centrum,srednia_kata,centrum_r1,centrum_g1,centrum_b1,kat_r1,kat_g1,kat_b1



    
t = [i for i in range(15,115,10)]
y = main(150,100,9,'zdj_day1',t)

krok = t[1] - t[0]

logt = map(lambda x: math.log2(x/krok),t)
logt = list(logt)
plt.figure(figsize=(15,6))
plt.scatter(y =y[2] ,x = logt,marker = '.',color = 'red')
plt.scatter(y = y[3],x = logt,marker = '.',color = 'green')
plt.scatter(y = y[4],x = logt,marker = '.',color = 'blue')




