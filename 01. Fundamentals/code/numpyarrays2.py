#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Creating Numpy Arrays

"""

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
b = np.array([np.arange(3), np.arange(3),np.arange(3)])
c = np.zeros([3, 3],float)
d = np.ones([3, 3])
e = np.random.random([3, 3])

print(a)
print(b)
print(c)
print(d)
print(e)
