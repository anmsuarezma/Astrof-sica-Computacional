""" 
Computational Astrophysics 
2019
Extra Exercise on Differentiation

We use a numerical differentiator for a known analytical function and 
compare the result with the value of the analytical derivative for different 
values of delta to evaluate the error

"""

import matplotlib.pyplot as plt
import numpy as np
from derivative import centeredDerivative
from derivative import forwardDerivative

  
# Definition of the analytic function to be differentitated
def f(x):     
    return x - np.sin(x) 

# Definition of the analytic derivative of the function 
def derf(x):     
    return 1 - np.cos(x) 


# Point x where we evaluate the derivatives
x0 = np.pi/4.

# value of the analytical derivative (is just one value!)
derivativex = derf(x0)

# Definition of the deltax values 
delta = np.arange(1e-6, 1e-10, -1e-10)

# Analytical derivative minus numerical derivative for  all deltax
epsilon_centered =  np.absolute(derivativex - centeredDerivative(f, x0, delta) )
epsilon_forward =  np.absolute(derivativex - forwardDerivative(f, x0, delta) )

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
plt.plot(delta , epsilon_centered, label="Centered derivative error")
plt.plot(delta , epsilon_forward, label="Forward derivative error")
plt.legend()
plt.show()

