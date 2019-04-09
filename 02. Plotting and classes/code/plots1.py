#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Plotting data from a file

"""

import matplotlib.pyplot as plt 
import numpy as np

file_name = "plotdata.txt" 
data = np.loadtxt(file_name, comments="#") 
x = data[:,0]
y = data[:,1]

# plot the data 
plt.plot(x,y) 
plt.show()