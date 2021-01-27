#!/usr/bin/env python3

import math
import turtle


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.delay(1)
    t = turtle.Turtle()
    t.setheading(90)
    t.color('red', 'green')
    pi = math.pi
    for k in range(0, 300):
        t.goto(200*math.sin(k*pi/13), 200*math.sin(k*pi/17))
    screen.mainloop()
