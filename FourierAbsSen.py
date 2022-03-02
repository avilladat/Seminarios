import numpy as np
import matplotlib.pyplot as plt
import math as m

def fourier(x,n):
    sum = 2/m.pi
    i = 1
    while (i <= n):
        sum += (-4/m.pi)/(4*i**2-1)*np.cos(2*i*x)
        i+=1
    return sum

N = 10000
ax = -m.pi
bx = m.pi

x = np.linspace(ax,bx,N)
y = np.abs(np.sin(x))

i = 2
while i <= 100 :
    yf = fourier(x,i)
    plt.plot(x,y)
    plt.plot(x,yf)
    plt.pause(0.1)
    if (i != 100) : plt.clf()
    i+=1
plt.show()
