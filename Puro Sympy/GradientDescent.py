import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x, y, lam = symbols('x y lam')

f = 8*(x**2) + 6*(y**2) + 4*(x-1)*(y-2)

def grad(f,xk):
    return np.array([diff(f,x).subs([(x,xk[0]),(y,xk[1])]),diff(f,y).subs([(x,xk[0]),(y,xk[1])])])

def step(f,xk):
    v = xk - lam*grad(f,xk)
    flam = f.subs([(x,v[0]),(y,v[1])])
    dflam = diff(flam,lam)
    lamk = solve(dflam,lam)
    return lamk

def descent(f,x,ite):
    xk = x
    xn = []
    lambk = step(f,xk)
    dk = -grad(f,xk)
    xn.append(xk + lambk*dk) 
    i = 0
    for i in range(ite-1):
        xk = xn[i]
        lambk = step(f,xk)
        dk = -grad(f,xk)
        xn.append(xk + lambk*dk) 
        i+=1
    print(xn)
    return xn

xn = descent(f,np.array([0.5,1.5]),10)

fx = lambdify([x,y],f)

N = 20
a = -1
b = 1

xl = np.linspace(a,b,N)
yl = np.linspace(a,b,N)

xmesh, ymesh = np.meshgrid(xl,yl,indexing='ij')
zmesh = fx(xmesh,ymesh)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(xmesh, ymesh, zmesh, alpha = 0.5)
for i in xn:
    ax.scatter(i[0], i[1], fx(i[0],i[1]), c='red')
plt.show()