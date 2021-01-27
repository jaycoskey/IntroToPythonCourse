#!/usr/bin/env python3

import random
import turtle


def forward_right(t, pcol, pwidth, fval, rval):
    t.color(pcol)
    t.width(pwidth)
    for k in range(0, 10):
        d = random.randint(3, 7)
        t.pendown()
        t.forward(d*fval/100)
        t.penup()
        t.forward((10-d)*fval/100)
    t.right(rval)


if __name__ == '__main__':
    window = turtle.Screen()
    t = turtle.Turtle()
    t.penup()
    t.goto(-200, -200)
    t.setheading(90)
    forward_right(t, 'red',   3, fval=400, rval=90)    
    forward_right(t, 'green', 6, fval=400, rval=90)    
    forward_right(t, 'blue',  9, fval=400, rval=90)    
    forward_right(t, 'black', 12, fval=400, rval=90)    
    window.mainloop()
