#!/usr/bin/env python3

import random
import turtle


def draw_line(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)


if __name__ == '__main__':
    window = turtle.Screen()
    t = turtle.Turtle()
    t.hideturtle()  # Don't show the turtle
    t.speed(0)  # Fastest
    t.width(3)
    SCALE = 75
    
    # Draw horizontal lines
    draw_line(t, -3*SCALE,   -SCALE, 3*SCALE,  -SCALE)
    draw_line(t, -3*SCALE,   +SCALE, 3*SCALE,  +SCALE)
 
    # Draw vertical lines
    draw_line(t,   -SCALE, -3*SCALE,  -SCALE, 3*SCALE)
    draw_line(t,   +SCALE, -3*SCALE,  +SCALE, 3*SCALE)

    window.mainloop()
