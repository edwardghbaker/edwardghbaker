# -*- coding: utf-8 -*-

"""

Write a program that takes as input the dimensions of a room and outputs the following:

Area of the floor
Amount of paint required to paint the walls
Volume of the room

"""

import numpy as np 
pi = np.pi 
from pint import UnitRegistry
ureg = UnitRegistry()




#%%  Define room class 

class Room:
    
    def __init__(self, dimensions = 40, cHeight = 300.0, shape = 'circular',
                 numCoats = 2, dist_units = 'parsec', m2_per_litre=13*ureg('meters**2/liter'), rounding = 2):
        
        """
        This code creates a room object with the properties; R.volRoom, R.areaFloor, R.areaWalls, R.volPaint_Walls. 
        
        If shape is rectangular 'dimensions' must be array type e.g. [3,4].
        
        If shape is circular 'dimensions' should be int or float type, if an array is passed then output will be an array. 
        
        Volumne of paint for the walls is always given in litres. 
        
        
        m2_per_litre from https://www.dulux.co.uk/en/products/dulux-easycare-kitchen-matt
        
        dimensions - the room dimensions or room radius, int float or two element array of int or float
        cHeight - ceiling height, int or float
        
        shape - string, 'circular' or 'rectangular'
        
        numCoats - int, the number of paint coats
        
        dist_units - string, the units of the dimension measurment eg meter or inch 
        m2_per_litre - int or flaot with units, the area a litre of paint can cover
        rounding - int, the number of decimal places you want the answer rounded to
        
        
        """
        
        
        self.dimensions = dimensions * ureg(dist_units)
        self.cHeight = cHeight * ureg(dist_units)
        self.shape = shape.lower()
        self.numCoats = numCoats
        self.area_per_litre = m2_per_litre.to(str(dist_units+'**2/liter'))
        self.rounding = rounding
        Room.DoCalc(self)
        
        
        try: Room.Rounding(self)
        except: pass
        
    def DoCalc(self):
        
        """
        This function is called in __init__ just runs all the calculations to assign the output variables.
        
        """
        
        if self.shape == 'rectangular':
            x = self.dimensions[0]
            y = self.dimensions[1]
            z = self.cHeight
            
            volRoom = x*y*z
            areaFloor = x*y
            areaWalls = 2*z*(x+y)
            
        elif self.shape == 'circular':
            r = self.dimensions
            z = self.cHeight
            
            volRoom = pi*(r**2)*z
            areaFloor = pi*r**2
            areaWalls = 2*pi*r*z
        else:
            print('error - shape input incorrect - must be rectangular or circular')
        
        volPaint_Walls = areaWalls*self.numCoats/self.area_per_litre
        self.areaWalls = areaWalls
        self.volRoom, self.areaFloor, self.volPaint_Walls = volRoom, areaFloor, volPaint_Walls
    
    def Rounding(self):
        
        """
        This funciton is only executed if rounding variable set to an int, as all the rounding fucntions require int type input.
        
        """
        
        
        self.volRoom = self.volRoom.round(self.rounding)
        self.areaFloor = self.areaFloor.round(self.rounding)
        self.areaWalls = self.areaWalls.round(self.rounding)
        self.volPaint_Walls = self.volPaint_Walls.round(self.rounding)
        
        
        
    
# R = Room()

# print(R.volRoom)
# print(R.areaFloor)
# print(R.areaWalls)
# print(R.volPaint_Walls)
        
            