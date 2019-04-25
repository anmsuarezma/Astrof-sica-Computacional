# Computational Astrophysics 
# 2019
#

# Solution Exercise 3.2
# Needs the Finite Differences Derivative Module

import numpy as np
from derivative import centeredDerivative
import matplotlib.pyplot as plt

# Definition of the function to derive
def f(x):
	return x - np.sin(x)

# Definition of the analytic derivative
def derf(x):
	return 1 - np.cos(x)

# Definition of the interval at which we want to calculate the derivative
x_min = -1.
x_max = 1.
n = 1000  # number of points within the interval

# Definition of the delta parameter
# Rule of thumb:sqrt(epsilon of the machine)
delta = 1e-8

# Discretized Interval
step = (x_max - x_min) /n
x = np.arange(x_min, x_max + step, step)

# Analytic Function and Derivative in  the interval
functionx = f(x)
derivativex = derf(x)

# Numerical Central Derivative in the interval
dfdx = centeredDerivative(f, x, delta)

# a) Plot analytical function and numerical derivative
plt.subplot(2,1,1)
plt.plot(x,functionx,label="y=f(x)")
plt.plot(x, dfdx,label="y=f'(x)")
plt.legend()
plt.grid(True)

# b) Plot analytical derivative and numerical derivative
plt.subplot(2,1,2)
plt.plot(x, dfdx,label="y=f'(x) (numerical)")
plt.plot(x, derivativex, '--', label="y=f'(x) (analytical)")
plt.legend()
plt.grid(True)
plt.show()


# Write the derivative data in a .txt file
data = np.column_stack((x,dfdx))
np.savetxt("outfile.txt", data, fmt="%10.10E",\
	header="Derivative of a function \n x f'(x)")
