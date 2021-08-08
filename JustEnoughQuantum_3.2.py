#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 11:57:53 2021

@author: georgios
"""

import math
import numpy as np
from numpy import linalg as LA    # The linear algerba library in numpy
#import qutip 

a_0 = complex(1/math.sqrt(2),0)
#a_1 = complex(1/math.sqrt(2),0)
a_1 = complex(0, 1/math.sqrt(2))

state_vector = np.array([
    [a_0],
    [a_1]
])
print(LA.norm(state_vector,2))  # 1.0 

#b = qutip.Bloch()
#up = qutip.basis(2,0)
#b.add_states(up)
#down = qutip.basis(2,1)
#b.add_states(down)
#b.show()

root_2 = math.sqrt(2)
transformation_matrix = np.array([
    [1/root_2 , - 1/root_2],
    [1/root_2,  1/root_2]
])
print(transformation_matrix)

state_vector = np.array([0,1]) 
results = transformation_matrix @ state_vector.T 
print(results)

#from util.blochsphere import BlochSphere
#b = BlochSphere()
#b.add_pt_by_alpha_beta(results[0], results[1], 'RESULT')
#b.add_pt_by_alpha_beta(0, 1, 'Original Vector')

a_0 = complex(1/math.sqrt(2),0)  
a_1 = complex(1/math.sqrt(2),0)

# I am setting up the |0> ket here.

KET = np.array([
    [a_0],
    [a_1]
])

print(KET)

BRA = KET.T.conj() 
# BRA is just the complex conjugate of the KET - the code is much simpler
print(BRA)
# array([[0.70710678-0.j, 0.70710678-0.j]])
# The L2 Norm is calculated as so.
print(LA.norm(BRA @ KET, 2)) # This equals 1

KET_0 = np.array([
    [1],
    [0]
])
KET_1 = np.array([
    [0],
    [1]
])
BRA_1 = KET_1.T.conj()
print(BRA_1)         # [[0 1]]
print(LA.norm(BRA_1 @ KET_0, 2)) # This equals zero

print(BRA_1 @ state_vector)   # [1]
print(KET_1 @ BRA_1 @ state_vector) # This gives [0 1] and not what the book says :
# array([[0.        +0.j],
#       [0.70710678+0.j]])
print(state_vector.T.conj())  # [0 1 ]
print(state_vector.T.conj() @ KET_1)  # [1] 
print(state_vector.T.conj() @ KET_1 @ BRA_1 ) # [0 1]
print(BRA_1 @ state_vector)  # [1] 
print( (state_vector.T.conj() @ KET_1) @ (BRA_1 @ state_vector) ) # 1 
#print(LA.norm(state_vector.T.conj() @ KET_1 @ BRA_1 @ state_vector,2))  # ValueError: Improper number of dimensions to norm.

ket_measure = np.array([
    [1/np.sqrt(2)],
    [1/np.sqrt(2)]
]) 
bra_measure = ket_measure.T.conj()
prob_measure = bra_measure @ KET_1 @ BRA_1 @ ket_measure
print(LA.norm(prob_measure,2)) # 0.49999

Unitary_Matrix = np.array([
    [0,1],
    [1,0]
])
print(Unitary_Matrix.T.conj()) # It is the same as the Unitary_Matrix himself 
print( Unitary_Matrix @ KET_0)

print(np.kron(KET,KET))
#[[0.5+0.j]
# [0.5+0.j]
# [0.5+0.j]
# [0.5+0.j]]
print(np.kron(KET_0,KET_0))
#[[1]
# [0]
# [0]
# [0]]
print(np.kron(KET_0,KET_1)) 
#[[0]
# [1]
# [0]
# [0]]
print(np.kron(KET_1,KET_0))
#[[0]
# [0]
# [1]
# [0]]
print(np.kron(KET_1,KET_1))
#[[0]
# [0]
# [0]
# [1]]

SWAP = np.array([
    [1,0,0,0],
    [0,0,1,0],
    [0,1,0,0],
    [0,0,0,1],
])
print(SWAP @ np.kron(KET_1,KET_0)) 
#[[0]
# [1]
# [0]
# [0]]
print(SWAP @ np.kron(KET_1,KET_1))
#[[0]
# [0]
# [0]
# [1]]

print("Exercise 1") 
CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
])
print(CNOT @ np.kron(KET_1,KET_0)) 
#[[0]
# [0]
# [0]
# [1]]
print(CNOT @ np.kron(KET_1,KET_1)) 
#[[0]
# [0]
# [1]
# [0]]
print("Exercise 2") 
print(KET @ BRA)
#[[0.5+0.j 0.5+0.j]
# [0.5+0.j 0.5+0.j]]