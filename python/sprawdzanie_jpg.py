import nd2
from matplotlib import pyplot as plt
from PIL import Image
import cv2
import numpy as np
import os

lista = os.listdir('nadnercza')
if '.DS_Store' in lista:
    lista.remove('.DS_Store')
plik = lista[0][4:7]
