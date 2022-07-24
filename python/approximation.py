import nd2
from matplotlib import pyplot as plt
import cv2
import numpy as np
from PIL import Image
import seaborn as sns
import math
from for_nd2_files import main
from scipy.optimize import curve_fit

f = nd2.ND2File('seria 3 ciemny/test070.nd2')
f3 = np.array(f)
t = [1,2,4,6,8,10,20,40,60,80,100,200,400,600,800,1000,2000,4000,6000,8000,10000]
krok = 8

logt = map(lambda x: math.log2(x/krok),t)
logt = list(logt)

# def func(t):
#     logt = map(lambda x: 1 / (1 + 1/(1+np.exp(-x)),t))
#     logt = list(logt)
#     return logt
  



main = main(47,210,10,'nowa_kamera_20.07/seria 2',t)

xdata = logt
ydata = main[4]

def sigmoid(x, L ,x0, k, b):
    y = L / (1 + np.exp(-k*(x-x0)))+b
    return (y)

p0 = [max(ydata), np.median(xdata),1,min(ydata)] # this is an mandatory initial guess

popt, pcov = curve_fit(sigmoid, xdata, ydata,p0, method='dogbox')

x = np.linspace(-3, 12, 21)
y = sigmoid(x, *popt)

plt.figure(figsize=(15,6))
plt.scatter(y = main[4],x = logt,marker = 'x',color = 'blue')



plt.figure(figsize=(15,6))
plt.scatter(y = main[4],x = logt,marker = 'x',color = 'blue')
plt.plot(x,y ,color = 'red')





model1 = np.poly1d(np.polyfit(xdata, ydata, 1))
plt.figure(figsize=(15,6))
plt.scatter(y = main[4],x = logt,marker = 'x',color = 'blue')
plt.plot(x,model1(x) ,color = 'red')

