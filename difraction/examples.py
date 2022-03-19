import matplotlib.pyplot as plt
import numpy as np
import math
import cmath
from scipy import integrate



def f(x, y, a,b):   #podint funct
    return np.exp(1/(2*b)*(x*x+(a-y)*(a-y)))


matr = open('matrix.txt','w') #file with matrix of raspred

l=0.005
s=10 #amount of points on y
st=10 #amount of points on z

g = np.zeros((s,st)) #our empty matrix

z = np.zeros(st)
y = np.zeros(s)

for i in range(1,s):
    y[i]=i
for k in range(1,st):
    z[k]=k
#z = np.linspace(0, 10, st) #point on z axe
#y = np.linspace(0,1,s) #point on y axe


for i in range(0,s):
    for k in range(0,st):
        args = [y[i],z[k]]
        v, err = integrate.dblquad(f, -1, 1, -np.inf, np.inf, args)
        g[i][k]=v*(np.exp(z[k])/z[k])
    print("it's ", i/10, "% of progress")
    

np.savetxt("matrix.txt", g, fmt='%.8e')
print(z,"\n", y,"\n",g)
#print(z)
#print(y)

