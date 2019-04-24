# Computational Astrophysics 
# 2019
#

# Solution 3.4
# Finite Differences Second Derivative Module

import numpy as np

def secondDerivative(f, x, delta):
    return (f(x + delta) - 2*f(x) + f(x - delta))/(delta**2)
