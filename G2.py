# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:22:52 2026

@author: alexg
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.close()

    # Create Grid
    coords = np.linspace(-10, 10, 101)
    x, y = np.meshgrid(coords, coords)

    # Create Function and gradient
    z = np.sqrt(x**2+y**2)
    dx, dy = np.gradient(z)  # Calculate the gradient

    # Create Figure
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('G2: 2D exponential function: $f(x,y)=\sqrt{x^2+y^2}$')

    # Plot scalar function as color plot (contour map)
    plt.contour(x, y, z, 20, cmap = "Greys") 
    plt.contourf(x, y, z, 100)  # plot a contour map using N=20 levels
    
    plt.set_cmap('coolwarm')  # change color of map

    # Plot Gradient as quiver plot
    skip = 5  # Number of points to skip

    # create coarse grid
    x_skipped, y_skipped = x[::skip, ::skip], y[::skip, ::skip]  # note the indexing [start:end:skip]
    dx_skipped, dy_skipped = dx.T[::skip, ::skip], dy.T[::skip, ::skip]  # note the .T transpose method

    # plot the gradient using the coarse grid and a quiverplot.
    plt.quiver(x_skipped, y_skipped, dx_skipped, dy_skipped, scale=3)
    plt.show()


if __name__ == '__main__':
    main()
