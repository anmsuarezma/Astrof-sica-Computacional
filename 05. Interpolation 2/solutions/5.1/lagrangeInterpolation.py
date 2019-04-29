'''
Computational Astrophysics 
2019

Solution 4.1
Lagrange Interpolation Method
'''

import numpy as np

#Lagrange Coefficients
def L(x, xi, j, n):
	prod = 1
	for k in range(n+1):
		if (k != j):
			prod = prod * (x - xi[k])/(xi[j] - xi[k])
	return prod

# Interpolated Polynomial
def p(x, xi, fxi, n):
	summ = 0
	for j in range(n+1):
		summ = summ + fxi[j]*L(x, xi, j, n)
	return summ
