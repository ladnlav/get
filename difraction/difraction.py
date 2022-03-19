import matplotlib.pyplot as plt
import numpy as np
import show
import math
from scipy import integrate
from matplotlib.streamplot import _integrate_rk12

def f(ksi,eta,p):
    return math.exp(ksi*ksi+(p-eta)*(p-eta))

s = 100
st = s*10

A0 = 15
lamda = 620
b = 1
g=np.zeros((s,st))

z = np.linspace(0, s, st)
y = np.linspace(0,b,s)


for i in range(0, s):
    for j in range(0,st):
        v, err = integrate.dblquad(f, 0, b, lambda eta: -100,100,args = (y[i]))
        g[i][j] = v

#plt.plot(z,y,g)
#plt.show()
