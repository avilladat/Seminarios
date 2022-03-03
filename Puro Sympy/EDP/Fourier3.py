import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math as math

x,n = symbols('x n')

def fourierFunction(f,a,b,m):
    a0 = simplify((1/((b-a)/2))*integrate(f,(x,a,b)))

    an = simplify((1/((b-a)/2))*integrate(f*cos(n*pi*x/((b-a)/2)),(x,a,b)))

    bn = simplify((1/((b-a)/2))*integrate(f*sin(n*pi*x/((b-a)/2)),(x,a,b)))

    suma = a0/2 + Sum(simplify(an*cos(n*pi*x/((b-a)/2)) + bn*sin(n*pi*x/((b-a)/2))),(n,1,m))

    fourier = lambdify(x,suma)
    fx = lambdify(x,f)
    
    xl = np.linspace(a,b,10000)
    y = fx(xl)
    yf = fourier(xl)
    plt.plot(xl,y)
    plt.plot(xl,yf)
    return

fsierra = Piecewise((x+1, And(x >= -1, x < 0)),
                    (x, And(x >= 0, x < 1)))

fcuadrada = Piecewise((1, And(x >= -1, x < -1/2)),
                      (-1, And(x >= -1/2, x < 0)),
                      (1, And(x >= 0, x < 1/2)),
                      (-1, And(x >= 1/2, x < 1)))

f3C = Piecewise((0, And(x >= -math.pi, x < 0)),
                (pi-x, And(x >= 0, x < math.pi)))

m = [10, 20, 50, 100, 1000]
'''
for i in m:
    fourierFunction(fsierra,-1,1,i)
    plt.savefig("C:/Users/PERSONAL/Documents/42/Documents/EAFIT/2022-1/Optimización 2/Seminario 1/Images/fouriersierra "+str(i))
    plt.close()

for i in m:
    fourierFunction(fcuadrada,-1,1,i)
    plt.savefig("C:/Users/PERSONAL/Documents/42/Documents/EAFIT/2022-1/Optimización 2/Seminario 1/Images/fouriercuadrada "+str(i))
    plt.close()
 
for i in m:
    fourierFunction(f3C,-math.pi,math.pi,i)
    plt.savefig("C:/Users/PERSONAL/Documents/42/Documents/EAFIT/2022-1/Optimización 2/Seminario 1/Images/fourier3C "+str(i))
    plt.close()
'''
'''
for i in m:
    fourierFunction(fsierra,-1,1,i)
plt.savefig("C:/Users/PERSONAL/Documents/42/Documents/EAFIT/2022-1/Optimización 2/Seminario 1/Images/fouriersierra todos")
plt.close()

for i in m:
    fourierFunction(fcuadrada,-1,1,i)
plt.savefig("C:/Users/PERSONAL/Documents/42/Documents/EAFIT/2022-1/Optimización 2/Seminario 1/Images/fouriercuadrada todos")
plt.close()

for i in m:
    fourierFunction(f3C,-math.pi,math.pi,i)
plt.savefig("C:/Users/PERSONAL/Documents/42/Documents/EAFIT/2022-1/Optimización 2/Seminario 1/Images/fourier3C todos")
plt.close()
'''    
