#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:31:55 2017

@author: eunmiko
"""

import numpy as np
 

class doublejex0104 :
    """ 
    the solution of the matrix equation 
    AXA'+CC' = X will be computed by
    these codes.
    
    A and C are (n-by-n) matrices
    whose eigenvalues are less than (or equal to) one.
    
    V = SUM (j for 0 to infty) np.dot(A**j, np.dot(C,C.T), A**j.T)
    
    We iterate to convergence on V(j) 
    starting from V(0) = np.dot(C,C.T) 
    
    Notice that the sum goes from 0 to infinity for j.
    
    The name of this code is based on "the doubling algorithm":
        the number of terms are doubled by each iteration
        
        V(0) = np.dot(C,C.T) 
        V(1) = V(0) + np.dot( np.dot(A, V(0)),A.T) # two terms
        a2 = A**2
        V(2) = V(1) + np.dot( np.dot(a2, V(1)), a2.T ) # four terms
        a3 = a2**2
        V(3) = V(2) + np.dot( np.dot(a3, V(2)), a3.T ) # eight 
        ...
        V(infty) until it converges
    
    
    We assure the convergence by the facts that eigenvalues
    of A and C lies within the unit circle. (bounded by the unity.)
    
    """
    def __init__(self, A, CCT):
        """
        Provide initial parameters describing the model.  
        All arguments should
        be Python scalars or NumPy ndarrays.

            * A is n x n
            * C is n x n  
            * both eigenvalues are bounded by the unity.
        """
        self.a1 = np.array(A, dtype='float32')
        self.V0 = np.array(CCT, dtype='float32')
        

    def doublej(self):
        
        a1, V0 = self.a1, self.V0
        
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
        
        print(V)
    
        return V