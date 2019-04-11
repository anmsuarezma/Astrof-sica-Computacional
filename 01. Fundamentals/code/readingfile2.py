#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Reading Files

"""

import numpy as np

# Open the file
infile = open("example_file2.txt","r")

# Read the data
indata = infile.readlines()

# Close the file again
infile.close()

print(indata)

# get number of data lines in the file 
# (-1, because first line is a comment) 
n = len(indata) - 1

# allocate two numpy arrays 
time = np.zeros(n)
data = np.zeros(n)

# parse the data 
for i in range(n):
	splitline = indata[i+1][:-1].split(',')
	time[i] = float(splitline[0])
	data[i] = float(splitline[1])

print(time)
print(data)