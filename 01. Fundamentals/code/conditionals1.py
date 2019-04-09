#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Conditional Statements

"""
import numpy as np

# get a random number in [0.0,1.0)
a = np.random.random()

if a < 0.5:
	print ("a = %5.6g is < 0.5!" % a) 
	print ("Small a!")
else:
	print ("a = %5.6g is >= 0.5!" % a) 
	print ("Large a!")