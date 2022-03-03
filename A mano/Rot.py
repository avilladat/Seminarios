import numpy as np
import matplotlib.pyplot as plt

def v(x,y,z):
    return np.array([y**2*z,-x*y,z**2])

def rotv(x,y,z):
    return np.array([0, y**2, -y-2*y*z])

N = 6
a = -1
b = 1

x = np.linspace(a,b,N)
y = np.linspace(a,b,N)
z = np.linspace(a,b,N)

xmesh, ymesh, zmesh = np.meshgrid(x,y,z,indexing='ij')
umesh, vmesh, wmesh = rotv(xmesh, ymesh, zmesh)
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.quiver(xmesh, ymesh, zmesh ,umesh, vmesh, wmesh, length = 0.3)
plt.show()