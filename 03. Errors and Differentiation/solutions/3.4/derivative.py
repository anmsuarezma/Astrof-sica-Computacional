# Computational Astrophysics 
# 2019
#

# Solution 3.1
# Finite Differences Derivative Module

import numpy as np

def forwardDerivative(f, x, delta):
    return (f(x + delta) - f(x))/delta

def backwardDerivative(f, x, delta):
    return (f(x) - f(x - delta))/delta

def centeredDerivative(f, x, delta):
    return (f(x + delta) - f(x - delta))/(2*delta)
