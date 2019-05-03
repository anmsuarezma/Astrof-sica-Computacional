'''
Computational Astrophysics 
2019

Solution 6.2 (part)
Needs the IntegratinMethods module
'''

import numpy as np
import matplotlib.pyplot as plt


# Definition of the function to be integrated
def f(x):
	return (x**2)/(np.exp(x) + 1)


x = np.arange(0, 50, 0.1)
f = f(x)

plt.plot(x,f)

# Plot Labels
plt.ylabel('f(x)')
plt.xlabel('x')

plt.savefig('plotIntegrand.pdf')
plt.show()



