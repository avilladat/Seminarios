import numpy as np
import matplotlib.pyplot as plt
import math as m

def fourier(x,n):
    sum = np.sinh(m.pi)/m.pi
    i = 1
    while i <= n:
        sum += ((2)/(m.pi))*((-1)**i)/((i**2)+1)*np.sinh(m.pi)*np.cos(i*x) - ((2)/(m.pi))*((-1)**i)/((i**2)+1)*i*np.sinh(m.pi)*np.sin(i*x)
        i+=1
    return sum

N = 10000
ax = -m.pi
bx = m.pi

x = np.linspace(ax,bx,N)
y = m.e**x

i = 1
while i <= 100 :
    yf = fourier(x,i)
    plt.plot(x,y)
    plt.plot(x,yf)
    plt.grid()
    plt.pause(0.1)
    if (i != 100) : plt.clf()
    i+=1
plt.show()