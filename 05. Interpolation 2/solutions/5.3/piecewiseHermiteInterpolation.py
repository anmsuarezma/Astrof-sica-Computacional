'''
Computational Astrophysics 
2019

Solution 5.3
Piecewise Hermite Interpolation Method
'''

import numpy as np

# Numerical Derivative
def derivative(xi, fxi):
	m = len(xi)
	dfxi = np.zeros(m)

	# First point
	dfxi[0] = (fxi[1] - fxi[0])/(xi[1] - xi[0])

	# Last point
	dfxi[m-1] = (fxi[m-1] - fxi[m-2])/(xi[m-1] - xi[m-2])

	# Intermediate points
	for i in range(1, m-1):
		dfxi[i] = (fxi[i+1] - fxi[i-1])/(2*(xi[i]-xi[i-1]))

	return dfxi

# Auxiliar functions for Hermite interpolation
def psi_0(z):
	return 2*z**3 - 3*z**2 + 1

def psi_1(z):
	return z**3 - 2*z**2 + z


# Hermite Interpolation 
def H3(x, x_i, f_i, df_i, x_i1, f_i1, df_i1):
	z = (x - x_i)/(x_i1 - x_i)
	H = f_i*psi_0(z) + f_i1*psi_0(1 - z) 
	+ df_i*psi_1(z)*(x_i1 - x_i) + df_i1*psi_1(1 - z)*(x_i1 - x_i)
	return H 


def pwHI(f, x_min, x_max, m, n):
	# Points for the piecewise interpolation
	# Note the step_m/2 added in the range construction to assure the 
	# apparition of the x_max point in the interval
	step_m = (x_max - x_min )/(m - 1)
	xi = np.arange(x_min,  x_max + step_m/2, step_m)
	fxi = f(xi)
	dfxi = derivative(xi, fxi)

	# Data Range 
	# Note the step_n/2 added in the range construction to assure the 
	# apparition of the x_max point in the interval
	step_n = (x_max - x_min) / (n - 1)
	data_x = np.arange(x_min, x_max + step_n/2, step_n)
	fx = f(data_x)

	# Array to store the interpolated data
	data_H3 = np.zeros(n)
	
	# Main loop to calculate the interpolated n-1 points
	for i in range(n-1):
		for j in range(m - 1):
			if (data_x[i] < xi[j+1]):
				data_H3[i] = H3(data_x[i], xi[j], fxi[j], dfxi[j], xi[j+1], fxi[j+1], dfxi[j+1])
				break
	# Last interpolated point is defined 
	data_H3[n-1] = fxi[m-1]
	return data_x, data_H3, fx

