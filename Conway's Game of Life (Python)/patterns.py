import numpy as np
"""
 Author: James A. Shackleford
   Date: Oct. 16th, 2015

   This file contains a few simple, well known patterns
"""

## Stills ###################################
block = [[0, 0, 0, 0],
         [0, 1, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]]

beehive = [[0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 0, 0],
           [0, 1, 0, 0, 1, 0],
           [0, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0]]

loaf = [[0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]]

boat = [[0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]]

tub = [ [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0] ]


## Oscillators ##############################
beacon = [ [1, 1, 0, 0],
           [1, 1, 0, 0],
           [0, 0, 1, 1],
           [0, 0, 1, 1] ]

blinker = [[0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0]]

turbine = [ [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0] ]


cloverleaf = [ [0, 0, 0, 1, 0, 1, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 1, 1, 0],
               [1, 0, 0, 0, 1, 0, 0, 0, 1],
               [1, 0, 1, 0, 0, 0, 1, 0, 1],
               [0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 1, 1, 0],
               [1, 0, 1, 0, 0, 0, 1, 0, 1],
               [1, 0, 0, 0, 1, 0, 0, 0, 1],
               [0, 1, 1, 1, 0, 1, 1, 1, 0],
               [0, 0, 0, 1, 0, 1, 0, 0, 0] ]

pulsar = [ [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
           [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0] ]

pentadecathlon = [ [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                   [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
                   [0, 0, 1, 0, 0, 0, 0, 1, 0, 0] ]

small_exploder = [ [0, 1, 0],
                   [1, 1, 1],
                   [1, 0, 1],
                   [0, 1, 0] ]

exploder = [ [1, 0, 1, 0, 1],       # Turns into a pulsar
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],]

toad = [ [0, 1, 1, 1],
         [1, 1, 1, 0] ]

## Spaceships ###############################
glider = [[0, 0, 1],
          [1, 0, 1],
          [0, 1, 1]]

hammerhead = [ [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
               [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

lwss = [ [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 1, 1, 1, 1]]

speed = [ [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 1, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 0, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0] ]

## Generators ###############################
gosper_gun = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
