import numpy as np
import matplotlib.pyplot as plt
import math as m

def fourier(x,n):
    sum = m.pi/4
    i = 1
    while (i <= n):
        sum += ((1-((-1)**i))/(m.pi*(i**2)))*np.cos(i*x) + (1/i)*np.sin(i*x)
        i+=1
    return sum

N = 10000
ax = -m.pi
bx = m.pi

x = np.linspace(ax,bx,N)
y = np.piecewise(x, [x<0 , x>=0], [lambda x: 0, lambda x: m.pi-x])

i = 1
while i <= 100 :
    yf = fourier(x,i)
    plt.plot(x,y)
    plt.plot(x,yf)
    plt.pause(0.1)
    if (i != 100) : plt.clf()
    i+=1
plt.show()