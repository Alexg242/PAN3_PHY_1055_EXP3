# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:12:39 2026

@author: alexg
"""

import matplotlib.pyplot as plt
import numpy as np
from G3_modifications import *

def main():
    plt.close('all')
    coords = np.linspace(-3, 3, 21)
    x, y = np.meshgrid(coords, coords)
    dx = y
    dy = -0.5*y-(1**2)*x
    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('G3: 2D Vector field Damped Harmonic Osccilator: $f(x,y)=(y, -\omega^2 x)$')
    plt.quiver(x, y, dx, dy)  # plot field as quiver
    plt.streamplot(x, y, dx, dy)
    plt.show()


# if this is the module called directly, then execute the main function, otherwise only define it
if __name__ == '__main__':
    main()
