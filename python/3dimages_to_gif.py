import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
import nd2
# generate some sample data
import scipy.misc
import os
import imageio

folder = 'wyrownanie_2'

pliki = sorted(os.listdir(folder))
if '.DS_Store' in pliki:
    pliki.remove('.DS_Store')
images = []
for i in range(len(pliki)):
    obraz = nd2.imread(f'wyrownanie_2/{pliki[i]}')
    obraz1 = obraz[0]
    lena = obraz1[:,:,2]
    
    # downscaling has a "smoothing" effect
    lena = cv2.resize(lena, (100,100))
    
    # create the x and y coordinate arrays (here we just use pixel indices)
    # create the x and y coordinate arrays (here we just use pixel indices)
    xx, yy = np.mgrid[0:lena.shape[0], 0:lena.shape[1]]
    
    # create the figure
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(xx, yy, lena ,rstride=1, cstride=1, cmap=plt.cm.gray,
            linewidth=0)
    
    ax.view_init(elev=50.)
    plt.savefig(f'zdjecia{i}.png')


    
    # show it
    plt.show()
    

for i in range(len(pliki)):
    images.append(imageio.imread(f'zdjecia{i}.png'))
    
    
imageio.mimsave('deep2.gif',images,**{'duration':0.5})


