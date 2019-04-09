#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Writes a table with the values of the wavelenghts for 
the n in the range between 3 and 15 of the Balmer series for the Hidrogen atom
"""

import mymodule as mym

print("\nn		lambda (m)")
for n in range(2,16):
	print (n,"		", mym.BalmerLines(n))

print()
