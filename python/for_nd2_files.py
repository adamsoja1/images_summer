import nd2
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import math
import os




def srednia(img):
    x = np.shape(img)[1]
    y = np.shape(img)[0]
    
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


def srednia_kat_prawyGorny(img):
    
    x = np.shape(img)[1]
    y = np.shape(img)[0]
    
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]
    
    box_r = red[1:100,x-100:x]
    box_g = green[1:100,x-100:x]
    box_b = blue[1:100,x-100:x]
    
    s1 = np.mean(box_r)
    s2 = np.mean(box_g)
    s3 = np.mean(box_b)
    arr = [s1,s2,s3]
    
    return np.array(arr)
    

def srednia_kat_prawyDolny(img):
        
    x = np.shape(img)[1]
    y = np.shape(img)[0]
    
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]
    
    box_r = red[y-100:y,x-100:x]
    box_g = green[y-100:y,x-100:x]
    box_b = blue[y-100:y,x-100:x]
    
    s1 = np.mean(box_r)
    s2 = np.mean(box_g)
    s3 = np.mean(box_b)
    arr = [s1,s2,s3]
    
    return np.array(arr)
    



def srednia_kat_lewyGorny(img):
    x = np.shape(img)[1]
    y = np.shape(img)[0]
    
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


def srednia_kat_lewyDolny(img):
    
    x = np.shape(img)[1]
    y = np.shape(img)[0]
    
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]
    
    box_r = red[y-100:y,1:100]
    box_g = green[y-100:y,1:100]
    box_b = blue[y-100:y,1:100]
    
    s1 = np.mean(box_r)
    s2 = np.mean(box_g)
    s3 = np.mean(box_b)
    arr = [s1,s2,s3]
    
    return np.array(arr)










def main(ilosc,seria,sciezka,t):
    
    iteracje = [i for i in range(1,ilosc+1)]
    
    srednia_centrum = []
    srednia_kata_prawyGorny = []
    srednia_kata_prawyDolny= []
    srednia_kata_lewyGorny= []
    srednia_kata_lewyDolny = []
    pliki = sorted(os.listdir(sciezka))
    if '.DS_Store' in pliki:
        pliki.remove('.DS_Store')
    
    for i in range(0,len(t)):
        obraz = nd2.imread(f'{sciezka}/{pliki[i]}')
        obraz1 = np.array(obraz)
        for j in range(0,seria):
            ob = obraz1[j]
            srednia_centrum.append(srednia(ob))
            srednia_kata_prawyGorny.append(srednia_kat_prawyGorny(ob))
            srednia_kata_prawyDolny.append(srednia_kat_prawyDolny(ob))
            srednia_kata_lewyGorny.append(srednia_kat_lewyGorny(ob))
            srednia_kata_lewyDolny.append(srednia_kat_lewyDolny(ob))
    
    
    temp = np.array(srednia_centrum)
    temp2_prawyGorny = np.array(srednia_kata_prawyGorny)
    temp2_prawyDolny = np.array(srednia_kata_prawyDolny)
    temp2_lewyGorny = np.array(srednia_kata_lewyGorny)
    temp2_lewyDolny = np.array(srednia_kata_lewyDolny)
    
    centrum_r = np.array(temp[:,0])
    centrum_g = np.array(temp[:,1])
    centrum_b = np.array(temp[:,2])
    
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
    
    
    
   
    
    
    
    
    plt.figure(figsize=(15,6))
    sns.scatterplot(y = centrum_r,x = iteracje,marker = '.',color = 'red')
    sns.scatterplot(y = centrum_g,x = iteracje,marker = '.',color = 'green')
    sns.scatterplot(y = centrum_b,x = iteracje,marker = '.',color = 'blue')

#
    
    
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

    

            
    
    j = seria - 1
    licznik = 0
    
    for i in range(0,len(t)):
        
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
        
    katy_r = [kat_r1_prawyGorny,kat_r1_prawyDolny,kat_r1_lewyDolny,kat_r1_lewyGorny]
    katy_g =[kat_g1_prawyGorny,kat_g1_prawyDolny,kat_g1_lewyDolny,kat_g1_lewyGorny]
    katy_b = [kat_b1_prawyGorny,kat_b1_prawyDolny,kat_b1_lewyDolny,kat_b1_lewyGorny]
    return srednia_centrum,centrum_r1,centrum_g1,centrum_b1,katy_r,katy_g,katy_b






def display_plots(y,t,krok,nazwaPliku):
    
    logt = map(lambda x: math.log2(x/krok),t)
    logt = list(logt)

    plt.figure(figsize=(15,11))
    plt.title('Kanały RGB dla centrum obrazu ')
    plt.scatter(y =y[1] ,x = logt,marker = 'x',color = 'red')
    plt.scatter(y = y[2],x = logt,marker = 'x',color = 'green')
    plt.scatter(y = y[3],x = logt,marker = 'x',color = 'blue')
    plt.ylabel('Wartość piksela')
    plt.xlabel('log2(t/t0)')
    plt.savefig(f'plots/centrum_obrazuRGB_{nazwaPliku}.png')
    
    
    
    
    
    
    plt.figure(figsize=(15,11))
    plt.title('Kanały R dla centrum obrazu ')
    plt.scatter(y =y[1] ,x = logt,marker = 'x',color = 'red')
    plt.ylabel('Wartość piksela')
    plt.xlabel('log2(t/t0)')
    plt.savefig(f'plots/centrum_obrazuR_{nazwaPliku}.png')
    
    
    
    
    plt.figure(figsize=(15,11))
    plt.title('Kanały G dla centrum obrazu ')
    plt.scatter(y = y[2],x = logt,marker = 'x',color = 'green')
    plt.ylabel('Wartość piksela')
    plt.xlabel('log2(t/t0)')
    plt.savefig(f'plots/centrum_obrazuG_{nazwaPliku}.png')
    
    
    
    
    plt.figure(figsize=(15,11))
    plt.title('Kanały B dla centrum obrazu ')
    plt.scatter(y = y[3],x = logt,marker = 'x',color = 'blue')
    plt.ylabel('Wartość piksela')
    plt.xlabel('log2(t/t0)')
    plt.savefig(f'plots/centrum_obrazuB_{nazwaPliku}.png')
    
    
    
    
    
    
    plt.figure(figsize=(15,11))
    plt.title('Kanał czerwony centrum obrazu porównanie z kątami obrazu ')
    plt.scatter(y = y[1],x = logt,marker = 'x',color = 'red')
    plt.scatter(y = y[4][0],x = logt,marker = 'x',color = 'black' )
    plt.scatter(y = y[4][1],x = logt,marker = 'x',color = 'blue' )
    plt.scatter(y = y[4][2],x = logt,marker = 'x',color = 'orange' )
    plt.scatter(y = y[4][3],x = logt,marker = 'x',color = 'green' )
    plt.legend(labels=['Centrum obrazu','Kąt prawy górny',"Kąt prawy dolny","Kąt lewy dolny ","Kąt lewy gorny"])
    plt.ylabel('Wartość piksela')
    plt.xlabel('log2(t/t0)')
    plt.savefig(f'plots/centrum_obrazuVSkatR_{nazwaPliku}.png')
    
    
    
    
    
    plt.figure(figsize=(15,11))
    plt.title('Kanał zielony centrum obrazu porównanie z kątami obrazu ')
    plt.scatter(y = y[2],x = logt,marker = 'x',color = 'red')
    plt.scatter(y = y[5][0],x = logt,marker = 'x',color = 'black' )
    plt.scatter(y = y[5][1],x = logt,marker = 'x',color = 'blue' )
    plt.scatter(y = y[5][2],x = logt,marker = 'x',color = 'orange' )
    plt.scatter(y = y[5][3],x = logt,marker = 'x',color = 'green' )
    plt.legend(labels=['Centrum obrazu','Kąt prawy górny',"Kąt prawy dolny","Kąt lewy górny ","Kąt lewy dolny"])
    plt.ylabel('Wartość piksela')
    plt.xlabel('log2(t/t0)')
    plt.savefig(f'plots/centrum_obrazuVSkatG_{nazwaPliku}.png')
    
    
    
    
    plt.figure(figsize=(15,11))
    plt.title('Kanał niebieski centrum obrazu porównanie z kątami obrazu ')
    plt.scatter(y = y[3],x = logt,marker = 'x',color = 'red')
    plt.scatter(y = y[6][0],x = logt,marker = 'x',color = 'black' )
    plt.scatter(y = y[6][1],x = logt,marker = 'x',color = 'blue' )
    plt.scatter(y = y[6][2],x = logt,marker = 'x',color = 'orange' )
    plt.scatter(y = y[6][3],x = logt,marker = 'x',color = 'green' )
    plt.legend(labels=['Centrum obrazu','Kąt prawy górny',"Kąt prawy dolny","Kąt lewy górny ","Kąt lewy dolny"])
    plt.ylabel('Wartość piksela')
    plt.xlabel('log2(t/t0)')
    plt.savefig(f'plots/centrum_obrazuVSkatB_{nazwaPliku}.png')
    
    
    
    fig1, axes = plt.subplots(2, 2, figsize=(15, 11))
    fig1.suptitle('Porównanie kanałów RGB z poszczególnych kątów obrazu', fontsize=16)
    
    axes[0,0].scatter(y = y[4][0],x = logt,marker = 'x',color = 'red' )
    axes[0,0].scatter(y = y[5][0],x = logt,marker = 'x',color = 'green' )
    axes[0,0].scatter(y = y[6][0],x = logt,marker = 'x',color = 'blue' )
    axes[0,0].legend(labels=['R','G',"B"])
    axes[0,0].set_ylabel('Wartość piksela')
    axes[0,0].set_xlabel('log2(t/t0)')
    axes[0,0].set_title("Kąt prawy górny")
    
    axes[0,1].scatter(y = y[4][1],x = logt,marker = 'x',color = 'red' )
    axes[0,1].scatter(y = y[5][1],x = logt,marker = 'x',color = 'green' )
    axes[0,1].scatter(y = y[6][1],x = logt,marker = 'x',color = 'blue' )
    axes[0,1].legend(labels=['R','G',"B"])
    axes[0,1].set_ylabel('Wartość piksela')
    axes[0,1].set_xlabel('log2(t/t0)')
    axes[0,1].set_title("Kąt prawy dolny")
    
    axes[1,0].scatter(y = y[4][2],x = logt,marker = 'x',color = 'red' )
    axes[1,0].scatter(y = y[5][2],x = logt,marker = 'x',color = 'green' )
    axes[1,0].scatter(y = y[6][2],x = logt,marker = 'x',color = 'blue' )
    axes[1,0].legend(labels=['R','G',"B"])
    axes[1,0].set_ylabel('Wartość piksela')
    axes[1,0].set_xlabel('log2(t/t0)')
    axes[1,0].set_title("Kąt lewy dolny")
    
    axes[1,1].scatter(y = y[4][3],x = logt,marker = 'x',color = 'red' )
    axes[1,1].scatter(y = y[5][3],x = logt,marker = 'x',color = 'green' )
    axes[1,1].scatter(y = y[6][3],x = logt,marker = 'x',color = 'blue' )
    axes[1,1].legend(labels=['R','G',"B"])
    axes[1,1].set_ylabel('Wartość piksela')
    axes[1,1].set_xlabel('log2(t/t0)')
    axes[1,1].set_title("Kąt lewy gorny")
    plt.savefig(f'plots/kątyObrazuRGB_{nazwaPliku}.png')



