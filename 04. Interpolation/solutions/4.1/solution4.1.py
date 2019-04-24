'''
Computational Astrophysics 
2019

Solution 4.1
Needs the lagrangeInterpoaltion module
'''

import numpy as np
import matplotlib.pyplot as plt
from lagrangeInterpolation import *


# Definition of the function 
def f(x):
	return 1/(25*x**2 + 1)

# Definition of the interval at which we want to interpolate
x_min = -1.
x_max = 1.

# Order of the polynomial
n = 10  

# Discretized Interval (Note that the step definition gives a total of n+1 points)
step = (x_max - x_min) /n
xi = np.arange(x_min, x_max + step, step)
fxi = f(xi)


# Data to be ploted
step2 = (x_max - x_min) /1000
data_x = np.arange(x_min, x_max + step2, step2)

# Interpolated polynomial and function data
px = p(data_x, xi, fxi, n)
fx = f(data_x)


plt.plot(data_x, px, label = "p(x)")
plt.plot(data_x, fx, label = "f(x)")
plt.legend()
plt.show()
