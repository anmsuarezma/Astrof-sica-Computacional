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


# defining Mars as a planet 
mars = Planet("Mars", 1.88, 0.107)

# attributes of Mars 
print(mars.orbit_period)
print(mars.mass)
