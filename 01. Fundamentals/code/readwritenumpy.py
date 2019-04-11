#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Reading and writting Files with Numpy

"""
import numpy as np

# read file
data = np.loadtxt("example_file3.txt",comments="#")
print(data)

# do something with data, e.g., square each entry 

data[: , :] = data [: , :]**2
print(data)

# write result 
np.savetxt("outfile3.txt",data,fmt="%10.10E",\
	header="This is a data file")