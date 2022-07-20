import nd2
from matplotlib import pyplot as plt
import cv2
import numpy as np
from PIL import Image
import seaborn as sns
import math




f = nd2.ND2File('nowa_kamera_20.07/seria 2/test068.nd2')
f = np.array(f)
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

f2 = f[0]
pp = srednia(f[0])

x = f2[:,:,1]