import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import integrate

def f(x, y, a,b):
    return math.exp(a * x * y/b)

args = [53,56]
v, err = integrate.dblquad(f, 1, 2, 1, 2, args)

print(v)
