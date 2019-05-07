'''
Computational Astrophysics 
2019

Solution 6.2 (part b)
Needs the IntegratinMethods module
'''

import numpy as np
import matplotlib.pyplot as plt

beta = 1/20. # constant energy of the environment in MeVs

# Definition of the function to be integrated
def f(H):
	return (H**2)/(np.exp(beta*H) + 1)

# MidPoint rule integration
def MP(f, Hi, Hf):
	Qi = ((Hf - Hi))*(f((Hf + Hi)/2) )
	return Qi

# Find the upper limit of the integral
H_max = 400.
tolerance = 1E-15
while f(H_max) > tolerance: 
	H_max = H_max + 1.

# Interval width 
DeltaH = 5.

# First interval for the integral
H_i = 0.
H_f = H_i + DeltaH

# Initial value for the integral intervals
Qi = np.array([MP(f, H_i, H_f)])

# Initial value for the Energy intervals
H = np.array(H_i + DeltaH/2)

# Main loop for integration of all intervals
while H_f <= H_max:
	H_i = H_f
	H_f = H_i + DeltaH
	Qi = np.append(Qi, MP(f, H_i, H_f))
	H = np.append(H, H_i + DeltaH/2)

# Integral has units of MeV^3, this factor converts to J^3
# 1MeV = 1.60218E-13 J
Qi = ((1.60218E-13)**3)*Qi

# Constant of proportionality
h_bar = 1.0545718E-34
c = 3E8
constant = (8*np.pi)/(2*np.pi*h_bar*c)**3

# Value of the density of electrons
nei = constant*Qi

ne = np.sum(nei)

print("\nThe value of the total number density of electrons is", ne, "\n")

plt.bar(H,nei, align='center', alpha=1)

# Plot Labels
plt.ylabel(r'$\frac{dn_{e^\pm}}{dE}$')
plt.xlabel('E')

plt.savefig('plotSpectrum.pdf')
plt.show()



