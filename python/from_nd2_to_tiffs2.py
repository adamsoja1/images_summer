import nd2
from matplotlib import pyplot as plt
import numpy as np
from for_nd2_files import srednia
import cv2
from PIL import Image
import os
import nd2

folder_from = 'nadnercza'


folder = 'Zdjęcia w formacie tiff'
zdjecia = 'Zdjecia nadnerczej'

sciezka = folder +'/'+ zdjecia

lista = os.listdir(folder_from)
if '.DS_Store' in lista:
    lista.remove('.DS_Store')
    
pliki = sorted(lista)


for i in range(len(pliki)):
    nazwa = pliki[i][4:7]
    obraznd = nd2.imread(f'{folder_from}/{pliki[i]}',dask = True)
    for j in range(len(obraznd)):
        tiff = obraznd[j]
        tiff2 = np.array(tiff)
        cv2.imwrite(f'{sciezka}/{nazwa}_{i}{j}.tiff',tiff2)
