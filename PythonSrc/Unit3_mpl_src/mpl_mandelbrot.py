#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def mandelbrot_iter_counts_lengthy(xmin, xmax, ymin, ymax, nx=500, ny=500, iter_max=500):
    dx = (xmax-xmin) / (nx-1)
    dy = (ymax-ymin) / (ny-1)
    xs = [xmin + i*dx for i in range(nx)]
    ys = [ymin + i*dy for i in range(ny)]

    result = []
    for y in ys:
        row = []  
        for x in xs:
            z = 0
            c = x + 1j*y            # Note: 1j = math.sqrt(-1)
            iter_divergence = iter_max
            for i in range(1, iter_max):
                z = z*z + c
                if abs(z) > 2:  # Divergence
                    iter_divergence = i
                    break
            row.append(iter_divergence)
        result.append(row)

    return result


def mandelbrot_iter_count(x, y, iter_max):
    z = 0
    c = x + 1j*y  # Note: 1j = math.sqrt(-1)
    iter_divergence = iter_max
    for i in range(1, iter_max):
        z = z*z + c
        if abs(z) > 2:  # Divergence
            iter_divergence = i
            break
    return iter_divergence


def mandelbrot_iter_counts(xmin, xmax, ymin, ymax, nx=500, ny=500, iter_max=500):
    dx = (xmax-xmin) / (nx-1)
    dy = (ymax-ymin) / (ny-1)
    xs = [xmin + i*dx for i in range(nx)]
    ys = [ymin + i*dy for i in range(ny)]

    result = [[mandelbrot_iter_count(x, y, iter_max) for x in xs] for y in ys]
    return result


if __name__ == '__main__':
    plt.figure()
    bounds_all = [-1.6,      0.6,  -1.1,     1.1]
    bounds_a   = [-1.0,     -0.5,   0.0,     0.3]
    bounds_b   = [-0.78,   -0.73,  0.02,    0.08]
    bounds_c   = [-0.752, -0.749,  0.031, 0.0335]
    (xmin, xmax, ymin, ymax) = bounds_a
    nx = 100
    ny = 100
    iter_max = 100
    plt.imshow(np.array(mandelbrot_iter_counts(xmin,xmax,ymin,ymax,nx,ny,iter_max)),
               extent=(xmin,xmax,ymin,ymax), origin='lower')
    plt.show()
