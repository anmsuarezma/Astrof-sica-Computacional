#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Curve Plotting

"""

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return t**2*np.exp(-t**2)

def g(t):
    return t*np.sin(2*t)

# range of the independent variable
# 50 points between 0 and 3
t = np.linspace(0, 3, 50)

# values of the function for the numbers in the range of t
y1 = f(t)
y2 = g(t)

# separate figures
plt.figure()

# First subplot
plt.subplot(2, 1, 1)
plt.plot(t, y1, 'r-', label='f(t) = t^2*exp(-t^2)')
plt.legend()

# Second subplot
plt.subplot(2, 1, 2)
plt.plot(t, y2, 'bo', label='g(t) = t*sin(2t)')
plt.legend()

# show the plot
plt.show()