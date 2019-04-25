# Computational Astrophysics 
# 2019
#

# Solution 3.1
# Needs the Finite Differences Derivative Module

import numpy as np
from derivative import forwardDerivative
from derivative import backwardDerivative
from derivative import centeredDerivative

# Definition of the function to derive
def f(x):
	return x - np.sin(x)

# Point at which we want to calculate the derivative
x0 = 0.0

# Definition of the delta parameter
# Rule of thumb:sqrt(epsilon of the machine)
delta = 1e-8


# Forward Derivative
print("\n Using the Forward difference, the derivative at x =", x, "gives:", 
	forwardDerivative(f, x0, delta))

# Backward Derivative
print("\n Using the Backwards difference, the derivative at x =", x, "gives:", 
	backwardDerivative(f, x0, delta))

# central Derivative
print("\n Using the Centered difference, the derivative at x =", x, "gives:", 
	centeredDerivative(f, x0, delta), "\n")
