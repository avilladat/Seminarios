import numpy as np
import matplotlib.pyplot as plt
import math as m
import sympy as sym

x,y,z = sym.symbols('x y z')

v = np.array([x**2-y**2,2*x*y])

gradientv = np.array([sym.diff(v[0],x), sym.diff(v[1],y)])
divf = gradientv[0] + gradientv[1]
print("Derivadas parciales de v:")
print(gradientv)
print("Divergencia de v:")
print(divf)

fv = sym.lambdify([x,y], v)

N = 20
a = -10
b = 10
x = np.linspace(a,b,N)
y = np.linspace(a,b,N)

xmesh, ymesh = np.meshgrid(x,y,indexing='ij')
umesh, vmesh = fv(xmesh,ymesh)

plt.figure()
plt.quiver(xmesh, ymesh, umesh, vmesh)
plt.show()