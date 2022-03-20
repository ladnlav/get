import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D
import cmath

def f(x, y):   #podint funct
    return I0*(lamda*(math.sin(math.pi*l/lamda*y/math.sqrt(x*x+y*y))))*(lamda*(math.sin(math.pi*l/lamda*y/math.sqrt(x*x+y*y))))

matr = open('matrix.txt','w') #file with matrix of raspred

I0=50
lamda = 620/1000000000
kof=2*math.pi/lamda
l=0.003
s=100  #amount of points on y
st=10000 #amount of points on z

g = np.zeros((s,st)) #our empty matrix

z = np.linspace(0.0,30000.0, st) #point on z axe
y = np.linspace(-100.0,100.0,s) #point on y axe


for i in range(0,s):
    for k in range(0,st):
        args = [y[i],z[k]]
        g[i][k]=f(z[k],y[i])
    print("it's ", i/s*100, "% of progress")
    

np.savetxt("matrix.txt", g, fmt='%.8e')
print(z,"\n", y,"\n",g)

C = plt.contour(z,y,g,3,colors='black')
plt.contourf(z,y,g,3)
plt.clabel(C, inline=1, fontsize=10)
plt.show()

#print(z)
#print(y)

