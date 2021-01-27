#!/usr/bin/env python3

import math
import turtle


def forward_right(t, fval, rval):
    # t.forward(fval)
    fractal(t, fval, 3, 1)
    t.right(rval)


def fractal(t, dist, depth, dir):
    if depth < 1:
        t.forward(dist)
        return
    fractal(t, dist/3, depth - 1, dir)
    t.left(60*dir)
    fractal(t, dist/3, depth - 1, dir)
    t.right(120*dir)
    fractal(t, dist/3, depth - 1, dir)
    t.left(60*dir)
    fractal(t, dist/3, depth - 1, dir)


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.delay(1)
    t = turtle.Turtle()
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.setheading(90)
    for k in range(0, 6):
        if k % 3 == 0:
            t.color('black')
        elif k % 3 == 1:
            t.color('red')
        elif k % 3 == 2:
            t.color('blue')
        else:
            assert(False)  # Unrecognized value
        forward_right(t, 150, 60)
    screen.mainloop()
