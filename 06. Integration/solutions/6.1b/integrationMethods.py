'''
Computational Astrophysics 
2019

Solution 6.1
Integration Methods
'''

import numpy as np

# MidPoint Rule 
def MP(f, xi):
	Q = 0.
	for j in range(len(xi) - 2):
		Qi = (xi[j + 1] - xi[j])*f((xi[j + 1] + xi[j])/2)
		Q = Q + Qi
	return Q


# Trapezoid Rule 
def trapRule(fi, xi):
	Q = 0.
	for j in range(len(xi) - 2):
		Qi = (xi[j + 1] - xi[j])*(fi[j +1] + fi[j])/2
		Q = Q + Qi
	return Q


# Simpson Rule 
def Simpson(f, xi):
	Q = 0.
	for j in range(len(xi) - 2):
		Qi = ((xi[j + 1] - xi[j])/6)*(f(xi[j]) + 4*f((xi[j + 1] + xi[j])/2) + f(xi[j + 1]))
		Q = Q + Qi
	return Q
