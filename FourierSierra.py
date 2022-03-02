import numpy as np
import matplotlib.pyplot as plt
import math as m

def fourier(x,n):
    sum = 1/2
    i = 1
    while (i <= n):
        sum += ((-1-np.cos(m.pi*i))/(m.pi*i))*np.sin(i*m.pi*x)
        i+=1
    return sum

N = 10000
ax = -10
bx = 10

x = np.linspace(ax,bx,N)
y = x - np.floor(x)
yf = fourier(x,8)
plt.plot(x,y)
plt.plot(x,yf)
plt.grid()
plt.show()
"""
i = 1
while i <= 10000 :
    yf = fourier(x,i)
    plt.plot(x,y)
    plt.plot(x,yf)
    plt.grid()
    plt.pause(0.01)
    if (i != 100) : plt.clf()
    i+=100
plt.show()
"""