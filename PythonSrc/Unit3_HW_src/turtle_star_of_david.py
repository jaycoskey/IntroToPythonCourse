#!/usr/bin/env python3

import math
import turtle 
from turtle import *


# window = turtle.Screen()
# turple = turtle.Turtle()


# Specific to triangles
def draw_triangle(edge_length, internal_angle):
    complementary_angle = 180 - internal_angle
    i = 0
    while i < 3:  # Specific to triangles
        forward(edge_length)
        left(complementary_angle)
        i += 1


def draw_triangle_at_orientation(edge_length, internal_angle, orientation):
    penup()
    left(orientation)
    forward(dist_to_apex)
    left(90 + 60)  # Specific to triangles
    pendown()
    draw_triangle(edge_length, internal_angle)  # Specific to triangles
    penup()
    return_to_standard_settings()


def return_to_standard_settings():
    # Use goto() and setheading() instead of the following
    #   left(30)
    #   forward(dist_to_apex)
    ####left(180 - orientation)
    goto(0, 0)
    #####setheading(0)
    pendown()


if __name__ == '__main__':
    edge_length = 100
    internal_angle = 60  # Specific to triangles
    center_height = edge_length / math.sqrt(3)  # Specific to triangles
    dist_to_apex = center_height  # Specific to triangles

    # The turtle starts out at the origin, facing right.
    # So the following two lines are not needed here:
    #     goto(0, 0)
    #     setheading(0)
    speed(1)
    for orientation in [30, 90]:  # Specific to triangles
        draw_triangle_at_orientation(edge_length, internal_angle, orientation)

    mainloop()
