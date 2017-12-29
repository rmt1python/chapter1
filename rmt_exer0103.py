#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:21:37 2017
File: rmt_exer0103.py

@author: rmt1python @ rochester econ 
/ had learned Python from Jon Stachulski and Tom Sargent in 2013 
/ @ SNU and taught myself using QuantEcon.org afterward.

Markov chain exercise

"""

import numpy as np
from numpy.linalg import inv 

beta = .95
gamma1 =  2.5  

# transition matrix


P1 = np.eye(2)
P2 = .5* np.ones((2,2))
pizero = .5 * np.ones((2,1))
cvec= np.array([1.,5.]).T
u = np.zeros((2))
u = cvec**(1.-gamma1)/(1.-gamma1)
v = np.zeros((2))
u = u.T


v1 = inv(np.eye(2) - beta*P1) @ u
bigv1 = pizero.T @ v1
v2 = inv(np.eye(2) - beta*P2) @ u
bigv2 = pizero.T @ v2

print('(1) when $\gamma$ = 2.5')
print('\n (interim) v1=')
print(v1)
print('\n (ex ante) V1')
print(bigv1)

print('\n (interim) v2=')
print(v2)
print('\n (ex ante) V2')
print(bigv2)


"""
"""

beta = .95
gamma1 = 4.0  

# transition matrix


u = np.zeros((2))
u = cvec**(1.-gamma1)/(1.-gamma1)
 

v1 = inv(np.eye(2) - beta*P1) @ u
bigv1 = pizero.T @ v1
v2 = inv(np.eye(2) - beta*P2) @ u
bigv2 = pizero.T @ v2

print('\n\nwhen $\gamma$ = 4.0')
print('\n (interim) v1=')
print(v1)
print('\n (ex ante) V1')
print(bigv1)

print('\n (interim) v2=')
print(v2)
print('\n (ex ante) V2')
print(bigv2)

