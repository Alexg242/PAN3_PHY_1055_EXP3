# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:22:13 2026

@author: alexg
"""



import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
from scipy import integrate

plt.rcParams['figure.dpi'] = 300


r = 1
K = 100

def main():
    r = 1 
    plt.close('all')
    plt.figure()
    Kvals = [100, 1000, 1500, 1230, 150, 500]
    for i in Kvals:    
        x = np.linspace(0, i*1.1,101)
        dx = r*x*(1 - x/i)
        plt.plot(x, dx, label="K = " + str(i))  # plot field as quiver

    plt.xlabel('x')
    plt.ylabel('dx')
    plt.title('G4: Collection of Population Model Derrivations: ' + r'$\frac{dx}{dt} = x\prime = rx(1 - \frac{x}{K})$')
    plt.axhline(y=0, color="k")
    plt.legend()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()
plt.show()


#%%

r = 1
K = 100


def main2():
    r = 1 
    plt.close('all')
    plt.figure()
    x = np.linspace(-10, K*1.1,101)
    dx = r*x*(1 - x/100)
    plt.plot(x, dx, label="K = " + str(K))  # plot field as quiver
    
    arrowsx = []
    arrowsy = []
    yvals = []
    c = []
    
    for i in dx:
        if i > 0:
            arrowsx.append(1)
            arrowsy.append(0)
            yvals.append(0)
            c.append('#FF0000')
        if i < 0:
            arrowsx.append(-1)
            arrowsy.append(0)
            yvals.append(0)
            c.append('#0000FF')

        if i == 0:
            arrowsx.append(0)
            arrowsy.append(0)
            yvals.append(0)
            c.append('#000000')

            
    plt.quiver(x, yvals, arrowsx, arrowsy, pivot='tail', scale = 35, color = c)
    
    plt.xlabel('x')
    plt.ylabel('dx')
    plt.title('G4: Population Model Derrivation With flow Respresentation: ' + r'$\frac{dx}{dt} = x\prime = rx(1 - \frac{x}{K})$')
    plt.axhline(y=0, color="k")
    plt.legend()
    
main2()
#%%

def pop(t, y, r, K):
    x = y
    dydt = r*x*(1 - x/K)
    return dydt

plt.close('all')
plt.figure()

def loop():
    # define the initial parameters
    x0 = 0# initial position
    v0 = 1# initial velocity
    y0 = (x0, v0)  # initial state
    t0 = 0  # initial time
    tf = 100  # final time
    n = 1001  # Number of points at which output will be e#valuated
    # creates an array of the time steps
    t = np.linspace(t0, tf, n)  # Points at which output will be evaluated

    Ks = [50, 100, 125]    
    rs = [0.2, 0.5, 1, 2]

    for i in Ks:
        
        lfun = lambda t, y, : pop(t, y, r=0.1, K=i)

        
        result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                                     t_span=(t0, tf),  # Initial and final times
                                     y0=y0,  # Initial state
                                     method="RK45",  # Integration method
                                     t_eval=t)  # Time points for result to be defined at
        # Read the solution and time from the result array returned by Scipy
        x, v = result.y
        t = result.t
        # plot position ad velocity as a function of time.
        plt.plot(t, v, label=r"K ="+ str(i) + ", r = " + str(r))
        
    for i in rs:
        
        lfun = lambda t, y, : pop(t, y, r=i, K=125  )

        
        result = integrate.solve_ivp(fun=lfun,  # The function defining the derivative
                                     t_span=(t0, tf),  # Initial and final times
                                     y0=y0,  # Initial state
                                     method="RK45",  # Integration method
                                     t_eval=t)  # Time points for result to be defined at
        # Read the solution and time from the result array returned by Scipy
        x, v = result.y
        t = result.t
        # plot position ad velocity as a function of time.
        plt.plot(t, v, label=r"K ="+ str(K) + ", r = " + str(i))



loop()
plt.xlabel('x')
plt.ylabel('y')
plt.title('G4: Collection of Population:' + r'$\frac{dx}{dt} = x\prime = rx(1 - \frac{x}{K})$')
plt.legend()