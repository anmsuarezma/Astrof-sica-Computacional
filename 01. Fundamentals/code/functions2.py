#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Functions

"""
def myfunction(x,y):
	return x**2, x + y

a = 2
b = 3

c,d = myfunction(a,b)

print(c)
print(d)