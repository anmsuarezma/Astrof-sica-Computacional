'''
Computational Astrophysics 
2019

Solution 5.1
Needs the lagrangeInterpoaltion module
'''

import numpy as np
import matplotlib.pyplot as plt
from lagrangeInterpolation import *

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

# Orders of the polynomials
N = np.array([6, 8, 10, 12])  

# Data Range 
m = 100 # Number of points to interpolate
step2 = (x_max - x_min)/(m-1)
data_x = np.arange(x_min, x_max + step2, step2)
print(data_x)

for n in N:
	# Discretized Interval (Note that the step definition gives a total of n+1 points)
	step = (x_max - x_min) /n
	xi = np.arange(x_min, x_max + step, step)
	fxi = f(xi)

	# Interpolated polynomial and function data
	px = p(data_x, xi, fxi, n)
	fx = f(data_x)
	
	# Calculate the EN2 and print the results
	print("\nThe value of EN2 for n=", n, "is:", EN2(px, fx, m), "\n")


