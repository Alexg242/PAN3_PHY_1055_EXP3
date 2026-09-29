# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:18:53 2026

@author: alexg
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300


def main():
    plt.close()
    x, y = np.meshgrid(np.linspace(0, 2 * np.pi, 101), np.linspace(0, 2* np.pi, 101))
    print(x, y)
    vx = np.cos(x)*y
    vy = np.sin(y)*x
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('G1: Quiver Plot Of Vx = y*cos(x), Vy = x*sin(y)')
    plt.quiver(x, y, vx, vy, pivot='mid', label='$v_x$ = $y$cos($x$), $v_y$ =$x$sin($y$)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()


#%%

a = np.linspace(1,10,10)
b = np.linspace(1, 5, 10)

c = a * b

print(c)