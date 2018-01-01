#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 13:02:37 2018
File: rmt_exer0105.py

@author: rmt1python @ rochester econ 
/ had learned Python from Jon Stachurski and Tom Sargent in 2013 
/ @ SNU and taught myself using QuantEcon.org afterward.
"""

import numpy as np
from rmt_doublej import doublejex0104

rho  = np.array([.8, -.3])
alpc = 1.
delta = np.array([.2, 0.])
gamma = np.array([0., 0.])
phi = np.array([.7, -.2])
beta = .95

"""
#(1)
psi1, psi2 = 1.,1.

"""
#(2)
psi1, psi2 = 2., 1.
 


 
row1 = np.append(np.append([rho], [delta] ), [alpc])
temp2 = np.vstack((row1, np.array([1., 0., 0., 0., 0.])))
row3 = np.append( np.append([gamma], [phi]), [0.])
temp3 = np.vstack((temp2, row3))
temp4 =  np.vstack((temp3, np.array([0., 0., 1., 0., 0.] )))
A = np.vstack((temp4, np.array([0., 0., 0., 0., 1.] )))

vec1c= np.array([psi1, 0., 0., 0., 0.]) 
vec2c=np.array([  0., 0.,psi2, 0., 0.])
C = np.vstack((vec1c, vec2c)).reshape(5,2)

temp0 = np.zeros((3,5))
Krow1 = np.array([-.5, 0., 0., 0., 30.])
temp = np.vstack((temp0, Krow1))
Krowend = np.array([30., 0., 0., 0., -1800.])
K = np.vstack((temp, Krowend))

lambdaa = np.linalg.eig(np.sqrt(beta)*A)[0]
if np.amax(lambdaa)>1.0:
        print("Eigenvalues exceed the unity.")
else:         
    print("\n\nA's eigenvalues are: ")
    print(lambdaa.round(decimals=4))

    print("\n\n")
    
temp = doublejex0104(np.sqrt(beta)*A, K)
B = temp.doublej()
d = np.array([beta* np.matrix.trace(B @ C @ C.T) / (1-beta)])
print("\nd=")
print(d)