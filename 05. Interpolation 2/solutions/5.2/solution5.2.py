'''
Computational Astrophysics 
2019

Solution 5.2
Needs the piecewiseLinearInterpolation module
'''

import numpy as np
import matplotlib.pyplot as plt
from piecewiseLinearInterpolation import *

# Error-Norm-2 Function
def EN2(p, f, m):
	summ = 0
	for i in range(m):
		summ = summ + ((p[i] - f[i])/(f[i]))**2
	return np.sqrt(summ)/m

# Definition of the function 
def f(x):
	return 1/(25*x**2 + 1)

# Definition of the interval at which we want to interpolate
x_min = -1.
x_max = 1.

# Number of points for the piecewise interpolation
m = 50

# Number of points to interpolate 
n = 100 

# Piecewise Linear Interpolation
data_x, data_p, fx = pwLI(f, x_min, x_max, m, n)

# Calculate the EN2 and print the result
print("\nThe value of EN2 for the piecewise linear interpolation is:", EN2(data_p, fx, n), "\n")

# Plot the function and the interpoated function 
plt.plot(data_x, data_p, label = "p(x)")
plt.plot(data_x, fx, '--', label = "f(x)")
plt.legend()
plt.show()
