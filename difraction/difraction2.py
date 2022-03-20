import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D

def f1(x,a,b):   #podint funct
    return np.exp(1j*kof/(2*b)*((a-x)*(a-x)))


def f2(x,a,b):   #podint funct
    return np.exp(1j*kof/(2*b)*(x*x))

matr = open('matrix.txt','w') #file with matrix of raspred

lamda = 620/1000000000
kof=2*math.pi/lamda
l=0.001
s=20  #amount of points on y
st=1000 #amount of points on z

g = np.zeros((s,st)) #our empty matrix
z0 = np.linspace(0.1, 10000.0, st) #point on z axe
y0 = np.linspace(-100.0,100.0,s) #point on y axe


for i in range(0,s):
    for k in range(0,st):
        #args = [y0[i],z0[k]]
        v1, err = integrate.quad(f1, -l/2, l/2,args = (y0[i],z0[k]))
        v2, err = integrate.quad(f2, -np.inf, np.inf,args = (y0[i],z0[k]))
        g[i][k]=v1*v2*(1/z0[k]/lamda)*(1/z0[k]/lamda)
    print("it's ", i/s*100, "% of progress")
    

np.savetxt("matrix.txt", g, fmt='%.8e')
print(z0,"\n", y0,"\n",g)

C = plt.contour(z0,y0,g,2,colors='black')
plt.contourf(z0,y0,g,2)
plt.clabel(C, inline=1, fontsize=10)
plt.show()

#print(z)
#print(y)

