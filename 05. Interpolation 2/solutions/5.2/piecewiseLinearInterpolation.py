'''
Computational Astrophysics 
2019

Solution 5.2
Linear Interpolation Method
'''

import numpy as np

# Linear Interpolation 
def p(x, x_i, f_i, x_i1, f_i1):
	return f_i + (f_i1 - f_i)*(x - x_i)/(x_i1 - x_i) 

def pwLI(f, x_min, x_max, m, n):
	# Points for the piecewise interpolation
	# Note the step_m/2 added in the range construction to assure the 
	# apparition of the x_max point in the interval
	step_m = (x_max - x_min )/(m - 1)
	xi = np.arange(x_min,  x_max + step_m/2, step_m)
	fxi = f(xi)
	
	# Data Range 
	# Note the step_n/2 added in the range construction to assure the 
	# apparition of the x_max point in the interval
	step_n = (x_max - x_min) / (n - 1)
	data_x = np.arange(x_min, x_max + step_n/2, step_n)
	fx = f(data_x)

	# Array to store the interpolated data
	data_p = np.zeros(n)
	
	# Main loop to calculate the interpolated n-1 points
	for i in range(n-1):
		for j in range(m - 1):
			if (data_x[i] < xi[j+1]):
				data_p[i] = p(data_x[i], xi[j], fxi[j], xi[j+1], fxi[j+1])
				break
	# Last interpolated point is defined 
	data_p[n-1] = fxi[m-1]
	return data_x, data_p, fx

