#!/usr/bin/env python3

import math
import turtle


def arc_position(center, radius, angle):
    radians = angle * math.pi / 180
    new_x = center[0] + radius * math.cos(radians)
    new_y = center[1] + radius * math.sin(radians)
    return (new_x, new_y)


def draw_arc(t, center, radius, from_angle, to_angle, steps):
    t.penup()
    for k in range(0, steps + 1):
        angle = from_angle + k * (to_angle - from_angle) / steps
        (x, y) = arc_position(center, radius, angle)
        t.goto(x, y) 
        t.pendown()


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.delay(0)

    angle_min = 10
    angle_max = 170
    arc_steps = 100
    radius_min = 100
    radius_max = 200
    radius_steps = 300
    t = turtle.Turtle()
    screen.colormode(1.0)  # Have color values lie between 0 and 1.0.
    for k in range(0, radius_steps + 1):
        radius = radius_min + k * (radius_max - radius_min) / radius_steps
        red   = max(0,  1 - 2 * k / radius_steps)    # 1-0-0
        green = max(0,  1 - math.fabs(k - 128)/128)  # 0-1-0
        blue  = max(0, -1 + 2 * k / radius_steps)    # 0-0-1
        t.color(red, green, blue)
        draw_arc(t, (0, 0), radius, 30, 150, arc_steps)

    screen.mainloop()
