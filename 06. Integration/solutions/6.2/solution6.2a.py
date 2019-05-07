'''
Computational Astrophysics 
2019

Solution 6.2
Needs the IntegratinMethods module
'''

import numpy as np
import matplotlib.pyplot as plt


# Definition of the function to be integrated
def f(x):
	return (x**2)/(np.exp(x) + 1)

# MidPoint rule integration
def MP(f, xi, xf):
	Qi = (xf - xi)*f((xf + xi)/2)
	return Qi

# Find the upper limit of the integral
x_max = 20.
tolerance = 1E-15
while f(x_max) > tolerance: 
	x_max = x_max + 1.

# Data Range 
h = 1E-5

# Lower limit for the integral
x_i = 0.
x_f = x_i + h

# Initial value for the integral
Q = 0.

while x_f <= x_max:
	Q = Q + MP(f, x_i, x_f)
	x_i = x_f
	x_f = x_i + h

print("\nThe value of the adimensional integral is", Q, "\n")

h_bar = 1.0545718E-34
c = 3E8
kT = 3.20435E-12
constant = (8*np.pi* kT**3)/(2*np.pi*h_bar*c)**3

ne = constant * Q 
print("\nThe value of the total number density of electrons is", ne, "\n")
