#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 18:08:21 2017

@author: ashcat
"""

""" 
Truncation Error - Convergence Test
We implement a 5th order accurate approximation of the function Sin(x)

We define a procedure that calculates the difference between the value of 
the Sin(x) function and the truncated approximation. 

Calculating the value of this epsilon for x<1 and then taking half of 
this value of x we show that the epsilon reduces by 2**5 = 32, 
demonstrating 5th-order accuracy
"""

import math as m
 
# Definition of the function giving the truncation error
def epsilon(x):
    return m.sin(x) - (x - (x**3)/6)

# Value to calculate the function
x = 0.1

# Results. We use the formating in the print function to show the results
print("\nFor x = %f the value of the truncation error is epsilon = %e" %( x, epsilon(x)))
print("For x = %f the value of the truncation error is epsilon = %e" %( x/2, epsilon(x/2)))
print("")
print("The ratio of these values is %f " %(epsilon(x)/epsilon(x/2)))
