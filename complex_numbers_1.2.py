#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 23:06:41 2021

@author: georgios
"""

import math
import cmath
import matplotlib.pyplot as plt
import pandas as pd

real = -1 * math.sqrt(0)
imaginary = 1 * math.sqrt(2)
z = complex(real,imaginary)
print(z)   ## (-0+1.4142135623730951j)

z2 = 3 + 4j
print(z2)    ## (3+4j)
print(z2*z2) ## (-7+24j) 
print(cmath.phase(z))  ## 1.5707963267948966  ## NOTE : the result on the LiveProject gives # 0.7853981633974483  !!!!!! 

z = complex(10,10)
y = complex(2,4)
x = z - y

c_numbers = [x,y,z]
for x in c_numbers:
    r, phi = cmath.polar(x)
    plt.polar([0,phi],[0,r], marker='o')
print(x)    # result (10 + 10j)

complex_numbers = [
    complex(1,1), 
    complex(2,1), 
    complex(6,3), 
    complex(-3,4), 
    complex(6,-1)
]
complex_sum1 = 0 + 0j
for cn in complex_numbers:
    complex_sum1 += cn 
print(complex_sum1)  ## (12+8j)
## We cannot use list comprehension for this sum, list comprehension is to generate a list, NOT to use the elements of an exiusting list in a sum.

for cn in complex_numbers:
    r, phi = cmath.polar(cn)
    plt.polar([0,phi],[0,r], marker='x')
