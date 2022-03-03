import numpy as np
import matplotlib.pyplot as plt
import math as m
from sympy import *
from sympy.vector import curl, CoordSys3D

R = CoordSys3D('R')

x,y,z = R.x, R.y, R.z

v = y**2*z*R.i - x*y*R.j + z**2*R.k
curlv = curl(v)

valores = lambda v,xmesh,ymesh,zmesh: [float(v.subs([(x,xmesh),(y,ymesh),(z,zmesh)]).dot(R.i)), float(v.subs([(x,xmesh),(y,ymesh),(z,zmesh)]).dot(R.j)), float(v.subs([(x,xmesh),(y,ymesh),(z,zmesh)]).dot(R.k))]
print(type(valores(curlv,1,2,3)[0]+1))

N = 6
a = -1
b = 1

xl = np.linspace(a,b,N)
yl = np.linspace(a,b,N)
zl = np.linspace(a,b,N)

xmesh, ymesh, zmesh = np.meshgrid(xl,yl,zl,indexing='ij')
umesh = vmesh = wmesh = [] 
for i,j,k in xmesh,ymesh,zmesh:
    val = valores(curlv,i,j,k)
    umesh.append(val[0])


