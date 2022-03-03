import numpy as np
import matplotlib.pyplot as plt

def v(x,y):
    return np.array([x**2-y**2,2*x*y])

N = 20

ax = -10
bx = 10
x = np.linspace(ax,bx,N)

ay = -10
by = 10
y = np.linspace(ay,by,N)

xmesh, ymesh = np.meshgrid(x,y,indexing='ij')
umesh, vmesh = v(xmesh,ymesh)

plt.figure()
plt.quiver(xmesh, ymesh, umesh, vmesh)
plt.show()