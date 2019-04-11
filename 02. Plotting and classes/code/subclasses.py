#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Defining a subclass

"""

import numpy as np

class Planet(object):
    def __init__ (self, planet_name, orbit_period, mass):
        self.name = planet_name 
        self.orbit_period = orbit_period  # in Earth years
        self.mass = mass # in units of Earth mass
    
    def semimajoraxis(self):
        '''
        returns the semimajor axis of the planet in AU
        calculated using Kepler's third law 
        '''
        return (self.orbit_period**(2./3.))

class Dwarf(Planet):
    def description(self):
        return self.name + " is a dwarf planet with a mass of " + str(self.mass) + " Earth masses."


# defining Pluto as a dwarf planet 
pluto = Dwarf("Pluto", 248.00, 0.00218)

# attributes of Pluto 
print(pluto.orbit_period)
print(pluto.mass)
print(pluto.semimajoraxis())
print(pluto.description())



