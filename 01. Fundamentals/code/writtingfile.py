#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Reading Files

"""

import numpy as np

# open the file for writting
outfile = open("outfile.txt","w")

# how many lines do we want to output 
n = 100

# write a header
headerstring = "# This is header for the data\n" 
outfile.write(headerstring)

# write some random data with a formatting
for i in range(n):
    ran1 = np.random.random()
    ran2 = np.random.random()
    outstring = "%10.10E,%10.10E\n" % (ran1,ran2) 
    outfile.write(outstring)

#close the file
outfile.close()