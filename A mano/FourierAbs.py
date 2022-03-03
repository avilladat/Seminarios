import numpy as np
import matplotlib.pyplot as plt
import math as m

def fourier(x,n):
    sum = m.pi/2
    i = 1
    while (i <= n):
        sum += ((2*np.cos(i*m.pi)-2)/(m.pi*(i**2)))*np.cos(i*x)
        i+=1
    return sum

N = 10000
ax = -m.pi
bx = m.pi

x = np.linspace(ax,bx,N)
y = np.abs(x)

i = 1
while i <= 50 :
    yf = fourier(x,i)
    plt.plot(x,y)
    plt.plot(x,yf)
    plt.grid()
    plt.pause(0.1)
    if (i != 50) : plt.clf()
    i+=1
plt.show()