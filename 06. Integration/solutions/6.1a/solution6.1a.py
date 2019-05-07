'''
Computational Astrophysics 
2019

Solution 6.1
Needs the IntegratinMethods module
'''

import numpy as np
from integrationMethods import *


# Definition of the function to be integrated
def f(x):
	return np.sin(x)

# Definition of the limits of the integral
a = 0.
b = np.pi
 

# Data Range 
n = 50000 # Number of intervals for the integration
h = (b - a)/(n-1)
x_i = np.arange(a, b + h/2, h)
f_i = f(x_i)

# Calculate the EN2 and print the results
print("\nThe value of the integral from", a, "to", b, "is:\n")
print("MidPoint Rule:\t\t", MP(f, x_i), "\n")
print("Trapezoidal Rule:\t", trapRule(f_i, x_i), "\n")
print("Simpson's Rule:\t\t", Simpson(f, x_i), "\n")

print(" h =", h, "\n")


