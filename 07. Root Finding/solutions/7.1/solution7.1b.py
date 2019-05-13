'''
Computational Astrophysics 
2019

Solution 7.1b
Solution of the eccentric anomaly equation using 
the Newton-Raphson method.
'''

import numpy as np


# Time to search and Initial value 
t = 365.25635 # days
E = np.pi/10.

# Problem Data for the Earth
a = 1 # semi-major axis in AU
ecc = 0.99999 # eccentricity
T = 365.25635 # Period in days

w = 2*np.pi/T # Angular frequency
b = a*np.sqrt(1 - ecc**2) # semi-minor axis in AU

# Definition of the function 
def f(E,t):
	return E - ecc*np.sin(E) - w*t 


# Definition of the derivative of the function 
def dfdx(E):
	return 1 - ecc*np.cos(E)

# Counter of iterations
n = 0
epsilon = 1E-15


# Main loop for root finding (Newton-Raphson)
while (np.absolute(f(E,t)) >= epsilon):
	E = E - f(E,t)/dfdx(E)
	n = n + 1


# Coordinates of the planet
x = a*np.cos(E)
y = b*np.sin(E) 


# Print the results
print("\nThe value of the eccentric anomaly at t=", t, " is E=", E, "\n")

print("\n The number of iterations needed is:", n, "\n")

print("\nThe coordinates of the planet at this moment are:\n x=", x, "and y=", y, "\n")

