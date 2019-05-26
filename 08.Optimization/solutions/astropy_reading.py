'''
Computational Astrophysics 
2019

Astropy example of reading data from a file
'''
from astropy.io import ascii
import numpy as np
import matplotlib.pyplot as plt

data = ascii.read("table1.dat",readme="ReadMe")  
logsigma = np.array(np.log10(data["sigma*"]))
logM = np.array(data["logM"])
#print(data)
#print(logsigma)
#print(logM)

plt.plot(logsigma,logM,".")
plt.show()
