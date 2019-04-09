#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Reading Files

"""

# Open the file
infile = open("example_file1.txt","r")

# Read the data
indata = infile.readlines()

# Close the file again
infile.close()

print(indata)