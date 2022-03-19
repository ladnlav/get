import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import integrate

def f(x, y, a,b):

    return np.exp(b)/b*np.exp(1/(2*b)*(x*x+(a-y)*(a-y)))

matr = open('example.txt','w')

l=2

g = np.zeros((1000,1000))
z = np.linspace(0, 100, 1000) 
y = np.linspace(0,1,1000)


for i in range(1,1000):
    for k in range(1,1000):
        args = [y[i],z[k]]
        v, err = integrate.dblquad(f, 0, l, -np.inf, np.inf, args)
        g[i][k]=v
    print("it's ", i/10, "% of progress")
print(g)
#print(z)
#print(y)

