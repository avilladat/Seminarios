import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

def descent(x=(np.array([0.5,1.5])), ite=10):
    xk = x
    xn = []
    lambk = step(xk)
    dk = -grad(xk)
    xn.append(xk + lambk*dk) 
    i = 0
    while(i < ite):
        xk = xn[i]
        lambk = step(xk)
        dk = -grad(xk)
        xn.append(xk + lambk*dk) 
        i+=1
    print(xn)
    return xn

def grad(xk):
    return np.array([16*xk[0] + 4*(xk[1] - 2), 4*(xk[0]-1) + 12*xk[1]])

def step(xk):
    x = xk[0]
    y = xk[1]
    return (-sqrt(-44*(x**2)+44*x*y+44*x+44*(y**2)-88*y
                  +81) + 34*x+14*y-9)/(8*(75*x+38*y-41))

xn = descent()

def f(x,y):
    return 8*(x**2) + 6*(y**2) + 4*(x-1)*(y-2)

N = 20
a = -1
b = 1

x = np.linspace(a,b,N)
y = np.linspace(a,b,N)

xmesh, ymesh = np.meshgrid(x,y,indexing='ij')
zmesh = f(xmesh,ymesh)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(xmesh, ymesh, zmesh, alpha = 0.5)
for i in xn:
    ax.scatter(i[0], i[1], f(i[0],i[1]), c='red')
plt.show()