from matplotlib import pyplot as plt
import cv2
import numpy as np
from PIL import Image
import seaborn as sns



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
    return np.array(arr)


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
    
    centrum_r = []
    centrum_g = []
    centrum_b = []
    kat_r = []
    kat_g = []
    kat_b = []
    
    
    
    srednia_centrum = np.array(srednia_centrum)
    j = seria
    
    for i in range(0,len(t)):

        centrum_r.append(np.mean(srednia_centrum[i:i+j][0]))
        centrum_g.append(np.mean(srednia_centrum[i:i+j][1]))
        centrum_b.append(np.mean(srednia_centrum[i:i+j][2]))
        
        kat_r.append(np.mean(srednia_kata[i:i+j][0]))
        kat_g.append(np.mean(srednia_kata[i:i+j][1]))
        kat_b.append(np.mean(srednia_kata[i:i+j][2]))

    

    plot1 = plt.scatter(y = centrum_r,x = t)
    
    
    return srednia_centrum,srednia_kata,centrum_r,centrum_g,centrum_b,plot1
    
t = [i for i in range(1,11)]
y = main(150,100,10,'zdj_day1',t)
