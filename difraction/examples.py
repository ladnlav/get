import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import integrate

def f(x, y):
    return x * y

v, err = integrate.dblquad(f, 1, 2, 1, 2)
print(v)
