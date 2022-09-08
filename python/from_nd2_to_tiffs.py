import nd2
from matplotlib import pyplot as plt
import numpy as np
from for_nd2_files import srednia
import cv2
from PIL import Image
import os
import nd2

folder_from = 'czas pracy/120'


folder = 'Tiff'
zdjecia = 'czas pracy/120'

sciezka = folder +'/'+ zdjecia

lista = os.listdir(folder_from)
if '.DS_Store' in lista:
    lista.remove('.DS_Store')
    
pliki = sorted(lista)


for i in range(len(pliki)):
    
    obraznd = nd2.imread(f'{folder_from}/{pliki[i]}')
    for j in range(len(obraznd)):
        tiff = obraznd[j]
        obraz = Image.fromarray(tiff)
        img = obraz.save(f'{sciezka}/{zdjecia}_{i}{j}.tiff')
