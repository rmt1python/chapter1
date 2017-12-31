#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:33:37 2017
File: rmt_exer0104.py

@author: rmt1python @ rochester econ 
/ had learned Python from Jon Stachurski and Tom Sargent in 2013 
/ @ SNU and taught myself using QuantEcon.org afterward.
"""


import numpy as np
from rmt_doublej import doublejex0104


'''
X_tplus1 = A @ X_t + C * w_tplus1
'''

"""
#(1)
rho = [1.2, -.3, 0.0, 0.0]
mu = 10.
c = 1.

#(2) 
rho = [1.2, -.3, 0.0, 0.0]
mu = 10.
c = 2.
 
"""
#(3)
rho = [.9, 0., 0., 0.]
mu = 5.
c = 1.

"""

#(4) 
rho = [.2, 0., 0., .5]
mu = 5.
c = 1.
 
#(5) 
rho = [.8, .3, 0., .0]
mu = 5.
c = 1.
"""

alpha = mu*(1.0-np.sum(rho,0))
temp = np.append([np.eye(3)], np.zeros((3,2)) )
subA = temp.reshape(5,3).T
temp1 = np.append([rho], [1.0])
temp2 = np.vstack((temp1, subA))
temp3 = np.append([np.zeros((1,4))], [1.0])
A = np.vstack((temp2,temp3))
lambdaa = np.linalg.eig(A)[0]
if np.amax(lambdaa)>1.0:
        print("Eigenvalues exceed the unity.")
else:         
    print("\n\nA's eigenvalues are: ")
    print(lambdaa)

    print("\n\n")

    C = np.array([c, .0, .0, .0, .0]).reshape(5,1)
    CCT = C @ C.T

    temp = doublejex0104(A, CCT)
    Cx0 = temp.doublej()
    
   
    #1.c
    A5 = np.linalg.matrix_power(A,5)
    print("\n\nFor 1.c \n ")
    muvec =np.array([mu, mu, mu, mu, 1]).reshape(5,1)
    betahat = np.linalg.inv(Cx0 + muvec @ muvec.T) @\
    (Cx0.T @ A5.T + muvec @ muvec.T)@\
    np.array([1., 0., 0., 0., 0.]).reshape(5,1)
    print(betahat.reshape(1,5))                 
    print("\n\nComparison")
    print(A5[0])
    
    # 1.d
    beta=.95
    H2 = np.array([1., 0., 0., 0., 0.])@\
    np.linalg.inv( np.eye(5)- (beta * A)) 
    print("\n\nFor 1.d \n ")
    print(H2.T)
    
    # 1.e
    print("\n\nFor 1.e \n ")
    print((Cx0 @ np.linalg.matrix_power(A,1).T)[1,1])
    print((Cx0 @ np.linalg.matrix_power(A,5).T)[1,1])
    print((Cx0 @ np.linalg.matrix_power(A,10).T)[1,1])
"""
Another inefficient way to form the matrix A

A = np.array([np.ndarray.tolist(np.append([rho], [1.0])),
     np.ndarray.tolist(subA[0,]),
     np.ndarray.tolist(subA[1,]),
     np.ndarray.tolist(subA[2,]),
     np.ndarray.tolist(np.append([np.zeros((1,4))], [1.0])) ])

"""

"""
def doublej(A,CCT):
        
        a1, V0 = A, CCT
        
        diff, ijk = 5, 1
    
        while diff>1e-15:
            V1 = V0 + ((a1 @ V0) @ a1.T)
            a2 = (a1 @ a1)
             
            diff = np.amax(np.amax(abs(V0-V1),1),0)
             
            V0 = V1
            a1 = a2
        
            ijk = ijk+1
        
            if ijk >50 :
                print("Error: check A and C for proper configuration")
    
        V=V0
        return V

V = doublej(A,CCT)
print(V)

# Lyapunouv theorem assures the unique existence of the solution 
# for V.
"""

