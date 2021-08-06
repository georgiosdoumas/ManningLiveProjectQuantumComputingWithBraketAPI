#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 23:44:54 2021

@author: georgios
"""

import math
import cmath
import matplotlib.pyplot as plt
import numpy as np 

a1 = np.array([[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]])
print(a1)
#[[1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]
# [1]]

# Create a vector of 1s
a2 = np.ones(9)
print(a2)  ## [1. 1. 1. 1. 1. 1. 1. 1. 1.] 
print(a2.shape)  ## (9,) 

# Create a vecotr with element from 1 to 9
b = np.arange(1,10)
print(b) ## [1 2 3 4 5 6 7 8 9] 

mat_a = np.array([
        [1,2],
        [3,4]  
])
print(mat_a.T)
#[[1 3]
# [2 4]]

mat_b = np.array([
    [4,5],
    [7,6]
])

print(mat_a + mat_b)
#[[ 5  7]
# [10 10]]

# Exercise 1 
m1 = np.array([ [math.sqrt(2)], [math.sqrt(2)], [math.sqrt(2)] ])
print(m1) 
#[[1.41421356]
# [1.41421356]
# [1.41421356]]
m2 = m1.T
print(m2)  # [[1.41421356 1.41421356 1.41421356]] 
print( m1 @ m2)
#[[2. 2. 2.]
# [2. 2. 2.]
# [2. 2. 2.]]

# Exercise 2 
m3 = np.array([ [complex(1,2)], [complex(2,3)], [complex(4,5)]  ])
print("m3 is \n" , m3) 
#[[1.+2.j]
# [2.+3.j]
# [4.+5.j]]
m4 = np.array([ 
        [ complex(1,2), complex(2,3), complex(4,5) ],
        [ complex(6,7), complex(4,1), complex(2,0) ] 
])
print("m4 is \n", m4)
# [[1.+2.j 2.+3.j 4.+5.j]
# [6.+7.j 4.+1.j 2.+0.j]]
#  multiplic = m3 @ m4  ## CAN NOT be executed! Error.
m5 = m4.T 
print("m4 transpose is \n", m5)
# multiplic = m3 @ m5  ## CAN NOT be executed! Error.
