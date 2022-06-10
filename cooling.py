# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:18:22 2020

@author: User
"""
import numpy as np

# def cooling(T,e_rpm,fan_%,fanrpm,bar,volt):
#     T
    
    
#     return


sp= 96. #Celcius
T0=0. 

voltf=100.
nsteps = 101

deltavolt= voltf/(nsteps-1)
ts = np.linspace(0,voltf,nsteps) #linearly spaced time vector
step = np.zeros(nsteps) 
es = np.zeros(nsteps)
ies = np.zeros(nsteps)
sp_store = np.zeros(nsteps)
ubias=0.0
Kc= 3
tauI =40.0
sum_int =0.0

if T < 96.:
    fan_% =0
    