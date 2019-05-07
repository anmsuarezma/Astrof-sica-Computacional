'''
Computational Astrophysics 
2019

Solution 6.1
Needs the IntegratinMethods module
'''

import numpy as np
import matplotlib.pyplot as plt
from integrationMethods import *


# Definition of the function to be integrated
def f(x):
	return np.sin(x)

# Analytic Integral of the function
def int_f(x):
	return -np.cos(x)

# Definition of the limits of the integral
a = 0.
b = np.pi
 
# Value of the analytic integral
intf = int_f(b) - int_f(a)

# Data Range 
N = np.arange(1E3, 1E5, 1E4) # Number of intervals for the integration
h = (b - a)/(N-1) # Values of parameter h for each n

MidPoint_data = np.zeros(len(h))
trapRule_data = np.zeros(len(h))
Simpson_data = np.zeros(len(h))


for j in range(len(h-1)):
	x_i = np.arange(a, b + h[j]/2, h[j])
	f_i = f(x_i)
	MidPoint_data[j] = MP(f, x_i)
	trapRule_data[j] = trapRule(f_i, x_i)
	Simpson_data[j] = Simpson(f, x_i)


# Error for each method
epsilon_MidPoint = (intf - MidPoint_data)/intf
epsilon_trapRule = (intf - trapRule_data)/intf
epsilon_Simpson = (intf - Simpson_data)/intf


# Plot the error in the integral with the three methods
plt.plot(h, epsilon_MidPoint, label = 'MidPoint Rule')
plt.plot(h, epsilon_trapRule, label = 'Trapezoid Rule')
plt.plot(h, epsilon_Simpson, label = 'Simpson\'s Rule')


# This command inverts the x axis
plt.gca().invert_xaxis()

# Plot Labels
plt.xlabel('h')
plt.ylabel('$\epsilon $')

# Set logarithmic axes to appreciate the error
plt.xscale('log')
plt.yscale('log')

plt.legend()

plt.savefig('epsilonvsh.pdf')
plt.show()


