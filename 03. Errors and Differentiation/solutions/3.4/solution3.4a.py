# Computational Astrophysics 
# 2019
#

# Solution 3.4 (Second Derivative at a point)
# Needs the Finite Differences Second Derivative Module

import numpy as np
from derivative2 import secondDerivative

# Definition of the function to derive
def f(x):
	return x - np.sin(x)

# Point at which we want to calculate the second derivative
x0 = 0.0

# Definition of the delta parameter
# Rule of thumb:sqrt(epsilon of the machine)
delta = 1e-8


# Second Derivative
print("\n The second derivative at x =", x, "gives:", 
	secondDerivative(f, x0, delta), "\n")
