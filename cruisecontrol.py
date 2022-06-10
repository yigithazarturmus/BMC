# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as odeint

#defining model

def vehicle(v,time,gaspedal,load):
    # v = velocity(m/s)
    #time = time(sec)
    #gaspedal = gaspedalposition(-%50 to%100)
    #load = passenger load + cargo (kg)
    Cd = 0.24    #drag coefficient
    rho = 1.225  # air density (kg/m^3)
    A = 5.0      #cross-sectional area (m^2)
    Fp = 30      # thrust parameter (N/%pedal)
    mass = 500   # vehicle mass (kg)
    dv_dt = (1.0/(mass+load)) * (Fp*gaspedal-0.5*rho*Cd*A*v**2)
    return dv_dt

tf = 300.0 #final time for simulation
nsteps = 301 #number of timne steps
delta_t = tf/(nsteps-1) #time of each step
ts = np.linspace(0,tf,nsteps) #linearly spaced time vector

#simulate step test operation
step = np.zeros(nsteps)  # gaspedal = valve % open

# passenger + cargo load
load= 200.0 #kg

#velocity inital condition
v0 = 0.0

#for storing the results
vs= np.zeros(nsteps)
ubias=0.0
Kc= 3
tauI =40.0
sum_int =0.0
es = np.zeros(nsteps)
ies = np.zeros(nsteps)
sp_store = np.zeros(nsteps)
sp=25

#simulate with ODIENT 
for i in range(nsteps-1):
    #schedule changes in setpoint
    if i ==50:
        sp=0
    if i ==100:
        sp=15
    if i ==150:
        sp=20
    if i== 200:
        sp=10
    sp_store[i+1] = sp
    error= sp-v0
    es[i+1]=error
    sum_int = sum_int + error*delta_t
    gaspedal = ubias + Kc*error + Kc/tauI * sum_int  

    # clip inputs to -50% to 100%
    if gaspedal >= 100.0:
        gaspedal = 100.0
        sum_int = sum_int - error*delta_t
    if gaspedal <= -50.0:
        gaspedal = -50.0
        sum_int = sum_int + error*delta_t
    ies[i+1] = sum_int
    step[i+1]=gaspedal  
    v = odeint.odeint(vehicle,v0,[0,delta_t],args=(gaspedal,load))    
    v0 = v[-1]  #taking the last value
    vs[i+1] = v0 #storing the velocity for plotting

#plot results
plt.figure()
plt.subplot(2,2,1)
plt.plot(ts,vs,'b-',linewidth=3)
plt.plot(ts,sp_store,'k--',linewidth=2)
plt.ylabel('velocity(m/s)')
plt.legend(['velocity','set point'],loc='best')
plt.subplot(2,2,2)
plt.plot(ts,step,'r--',linewidth=3)
plt.ylabel('gas pedal')
plt.legend(['gas pedal(%)'],loc='best')
plt.subplot(2,2,3)
plt.plot(ts,es,'b-',linewidth=3)
plt.legend(['error (sp-pv)'])  
plt.xlabel('time(sec)')
plt.subplot(2,2,4)
plt.plot(ts,ies,'k--',linewidth=3)
plt.legend(['integral of error'])
plt.xlabel('time(sec)')
plt.show()



    




    
    