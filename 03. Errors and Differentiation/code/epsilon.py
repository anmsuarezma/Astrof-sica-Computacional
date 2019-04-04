#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 3 2019

@author: ashcat
"""

""" 
Roundoff Error
We find the value of epsilon for which 1. + epsilon = 1.

This gives the machine epsilon value, representing the error inherent to
representing a floating point number

"""

epsilon = 1. # Initial value for epsilon

while (1. + epsilon != 1.):
    epsilon = epsilon /2.

print (epsilon)
 
# Iterates, halving epsilon until 1. + epsilon = 1.
# Prints the value of the machine epsilon
 