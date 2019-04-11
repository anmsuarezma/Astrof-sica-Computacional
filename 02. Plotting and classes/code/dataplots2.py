#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Plotting data from a file with some formatting

"""

import matplotlib.pyplot as plt 
import numpy as np

file_name = "plotdata.txt" 
data = np.loadtxt(file_name, comments="#") 
x = data[:,0]
y1 = data[:,1]
y2 = data[:,2]

# make the plots
fig, ax = plt.subplots()
p1 = ax.plot(x, y1, "r", linewidth = 2)
p2 = ax.plot(x, y2, "b", linewidth = 2)

# labels of the plot
ax.set(xlabel="X", ylabel="Y",
       title="Title of the plot")

# set x and y ranges 
plt.xlim(min(x),max(x)) 
plt.ylim(min(y1*1.05),max(y1*1.05))

# plot's grid
ax.grid()

# show the plot
plt.show()


# save the plot as a pdf or png
fig.savefig("simpleplot.pdf")
fig.savefig("simpleplot.png")
