#!/usr/bin/env python3

import math
import turtle


def forward_right(t, fval, rval):
    t.forward(fval)
    t.right(rval)


def sine_ish(move_num):
    return 45 + 90 * math.sin(math.pi * move_num / 25)


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.delay(1)
    t = turtle.Turtle()
    t.penup()
    t.goto(-200, 150)
    t.pendown()
    t.fillcolor('yellow')
    t.setheading(90)
    for move_num in range(0, 200):
        if move_num < 50:
            t.color('red')
        elif move_num < 100:
            t.color('green')
        elif move_num < 150:
            t.color('blue')
        else:
            t.color('black')
        forward_right(t, 30, sine_ish(move_num))
    screen.mainloop()
