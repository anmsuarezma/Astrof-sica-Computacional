# Computational Astrophysics 
# 2019
#

# Solution Exercise 3.4 (Second Derivative in an interval)
# Needs the Finite Differences Second Derivative Module

import numpy as np
from derivative import centeredDerivative
from derivative2 import secondDerivative
import matplotlib.pyplot as plt

# Definition of the function to derive
def f(x):
	return x - np.sin(x)

# Definition of the analytic derivative
def derf(x):
	return 1 - np.cos(x)

# Definition of the analytic second derivative
def derf2(x):
	return np.sin(x)

# Definition of the interval at which we want to calculate the derivative
x_min = -1.
x_max = 1.
n = 1000  # number of points within the interval

# Definition of the delta parameter
# Rule of thumb:sqrt(epsilon of the machine) but due
# to the squared delta in the denominator we use sqrt(sqrt(epsilon))
delta = 1e-4

# Discretized Interval
step = (x_max - x_min) /n
x = np.arange(x_min, x_max + step, step)

# Analytic Function, first and second Derivatives in the interval
functionx = f(x)
derivativex = derf(x)
derivative2x = derf2(x)

# Numerical Central Derivative in the interval
dfdx = centeredDerivative(f, x, delta)
dfdx2 = secondDerivative(f, x, delta)

# a) Plot analytical function and numerical first and second derivatives
plt.subplot(2,1,1)
plt.plot(x, functionx,label="y=f(x)")
plt.plot(x, dfdx,label="y=f'(x)")
plt.plot(x, dfdx2,label="y=f''(x)")
plt.legend()
plt.grid(True)

# b) Plot analytical derivative and numerical derivative
plt.subplot(2,1,2)
plt.plot(x, dfdx2,label="y=f''(x) (numerical)")
plt.plot(x, derivative2x, '--', label="y=f''(x) (analytical)")
plt.legend()
plt.grid(True)

plt.show()

