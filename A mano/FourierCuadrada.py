import numpy as np
import matplotlib.pyplot as plt
import math as m

def fourier(x,n):
    sum = 0
    i = 1
    while i <= n:
        sum += ((2*np.cos(m.pi*i)-4*np.cos(m.pi*i/2)+2)/(m.pi*i))*np.sin(i*m.pi*x)
        i+=1
    return sum

N = 10000
ax = 0
bx = 1

x = np.linspace(ax,bx,N)
y = np.piecewise(x, [x<1/2 , x>=1/2], [lambda x: 1, lambda x: -1])

i = 1
while i <= 100 :
    yf = fourier(x,i)
    plt.plot(x,y)
    plt.plot(x,yf)
    plt.grid()
    plt.pause(0.01)
    if (i != 100) : plt.clf()
    i+=1
plt.show()
