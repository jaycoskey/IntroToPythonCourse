#!/usr/bin/env python3

import math
import turtle


def forward_right(t, fval, rval):
    t.forward(fval)
    t.right(rval)


if __name__ == '__main__':
    window = turtle.Screen()
    t = turtle.Turtle()
    t.setheading(90)
    POINTS = 12 
    for k in range(0, POINTS):
        forward_right(t, 200, math.floor((POINTS - 1) / 2) * 360/POINTS)    
    window.mainloop()
