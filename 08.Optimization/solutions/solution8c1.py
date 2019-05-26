'''
Computational Astrophysics 
2019

Solution 8.1
Linear Fitting to astronomical data.
M_BH - sigma* relation
Greene and Ho (2016)

c) Fit, including errors
'''

from astropy.io import ascii
import numpy as np
import matplotlib.pyplot as plt

def linearFit(yi, xi, sigmayi, sigmaxi, dydx = 0.):
	# sigma function for the fit
	sig2 = sigmayi**2 + (dydx*sigmaxi)**2

	# Linear fit functions:
	sumx = sum(xi/sig2)
	sumy = sum(yi/sig2)
	sumx2 = sum(xi**2/sig2)
	sumxy = sum(xi*yi / sig2)
	s = sum(1.0/sig2)

	# Linear fit parameters
	a1 = (sumy*sumx2 - sumx*sumxy) / \
	     (s*sumx2 - sumx**2)

	a2 = (s*sumxy - sumx*sumy) / \
	     (s*sumx2 - sumx**2)
	
	# Uncertainties in the parameters of the fit     
	sigma_a1 = np.sqrt(sumx2/(s*sumx2 - sumx**2))
	sigma_a2 = np.sqrt(s/(s*sumx2 - sumx**2))
	return a1, a2, sigma_a1, sigma_a2


# astropy is used to read data from downloaded files
data = ascii.read("table1.dat",readme="ReadMe")  

# We will fit the function 
# logM = alpha + beta log(sigma*/sigma_0)

# Following the paper by Greene and Ho, we introduce 
# the value of \sigma_0 = 200 km/s
# as a reference to normalize the sigma* data
sigma_0 = 200.0

# Assign data to numpy arrays
logsigma = np.array(np.log10(data["sigma*"]/sigma_0))
logM = np.array(data["logM"])

# Assign error data to numpy arrays
e_logsigma = np.array(np.log(data["e_sigma*"]/sigma_0))
e_logM = np.array(data["e_logM"])

# number of points in the data
n = len(logM)


# Fit including errors sigma_y 
alpha, beta, sigma_alpha, sigma_beta = \
linearFit(logM,logsigma, e_logM, e_logsigma, 0.)


# print and visualize data and fit
print()
print('--------------------------------------------------------------')
print('Parameter for the Linear fit with errors')
print('alpha =', alpha)
print('beta =', beta)
print('sigma_alpha =', sigma_alpha)
print('sigma_beta =', sigma_beta)
print('--------------------------------------------------------------')
print()

xmin = np.min(logsigma)
xmax = np.max(logsigma)
x = np.linspace(xmin,xmax,100)

plt.plot(logsigma,logM,".")
plt.plot(x,  alpha + x*beta,"-",color="black", label='Central Fit')
plt.plot(x,  (alpha + sigma_alpha) + x*(beta ),"--",color="red", label=r'Central Fit + $\sigma_{\alpha}$')
plt.plot(x,  (alpha - sigma_alpha) + x*(beta ),"--",color="red", label=r'Central Fit - $\sigma_{\alpha}$')

plt.xlabel(r'$\log (\sigma * / \sigma_0)$')
plt.ylabel(r'$\log (M_{BH} / M_{\odot })$')
plt.legend()
plt.savefig('M-sigma_with_errorM.pdf')
plt.show()
