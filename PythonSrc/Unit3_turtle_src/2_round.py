#!/usr/bin/env python3

import turtle


def forward_right(t, fval, rval):
    t.forward(fval)
    t.right(rval)


if __name__ == '__main__':
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.setheading(90)
    POINTS = 12 
    for k in range(0, POINTS):
        forward_right(t, 50, 360/POINTS)    
    screen.mainloop()
