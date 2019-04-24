""" 
Computational Astrophysics 
2019
Extra Exercise on Differentiation

We use a numerical differentiator for a known analytical function and 
compare the result with the value of the analytical second derivative for different 
values of delta to evaluate the error

"""

import matplotlib.pyplot as plt
import numpy as np
from derivative2 import secondDerivative

  
# Definition of the analytic function to be differentitated
def f(x):     
    return x - np.sin(x) 

# Definition of the analytic second derivative of the function 
def derf2(x):     
    return np.sin(x) 


# Point x where we evaluate the derivatives
x0 = np.pi/4.

# value of the analytical second derivative (is just one value!)
derivativex2 = derf2(x0)

# Definition of the deltax values 
delta = np.arange(1e-4, 1e-10, -1e-10)

# Analytical derivative minus numerical second derivative for all deltax
epsilon =  np.absolute(derivativex2 - secondDerivative(f, x0, delta) )

# Plot Labels
plt.xlabel('$\delta$x ')
plt.ylabel('$\epsilon$')

# This command inverts the x axis
plt.gca().invert_xaxis()

# Set logarithmic axes to appreciate the error
plt.xscale('log')
plt.yscale('log')


# Plot the values of deltax vs the difference between analytical and 
# numerical derivatives
plt.plot(delta , epsilon)
plt.show()

