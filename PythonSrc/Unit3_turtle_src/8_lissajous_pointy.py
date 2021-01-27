#!/usr/bin/env python3

import math
import turtle


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.delay(1)
    t = turtle.Turtle()
    t.setheading(90)
    pi = math.pi
    for k in range(0, 200):
        t.penup()
        t.goto(200*math.sin(k*pi/17), 200*math.sin(k*pi/23))
        t.pendown()
        t.goto(200*math.sin(k*pi/19), 200*math.sin(k*pi/29))
    screen.mainloop()
