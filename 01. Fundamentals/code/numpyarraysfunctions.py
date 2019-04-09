#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Creating Numpy Arrays

"""

import numpy as np

a = np.random.random([3, 4])

print(a)
print(np.ndim(a))	# Number of dimensions
print(len(a))		# Size of the first dimension
print(len(a[0, :]))	# Size of the second dimension
print(a.max())		# Max entry
print(a.min())		# Min entry
print(a.sum())		# Sum of all the elements
print(a[0,:].sum()) # Sum of first row
print(a[:,0].sum()) # Sum of first column