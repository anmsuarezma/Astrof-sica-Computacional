#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23 Dec 2018

@author: ashcat

Plot animation

"""

import numpy as np


class Planet(object):
    def __init__ (self, planet_name, orbit_period, mass):
        self.planet_name = planet_name 
        self.orbit_period = orbit_period  # in Earth years
        self.mass = mass # in units of Earth mass
    
    def semimajoraxis(self):
        '''
        returns the semimajor axis of the planet in AU
        calculated using Kepler's third law 
        '''
        return (self.orbit_period**(2./3.))


# defining Mars as a planet 
mars = Planet("Mars", 1.88, 0.107)

# attributes of Mars 
print(mars.orbit_period)
print(mars.mass)
print(mars.semimajoraxis())

# defining Mars as a planet 
earth = Planet("Earth", 1., 1.)

# attributes of Mars 
print(earth.orbit_period)
print(earth.mass)
print(earth.semimajoraxis())

