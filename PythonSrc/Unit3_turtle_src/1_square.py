#!/usr/bin/env python3

import turtle


def forward_right(t, fval, rval):
    t.forward(fval)
    t.right(rval)


if __name__ == '__main__':
    window = turtle.Screen()
    t = turtle.Turtle()
    t.setheading(90)
    for k in range(0, 4):
        forward_right(t, fval=50, rval=90)    
    window.mainloop()
