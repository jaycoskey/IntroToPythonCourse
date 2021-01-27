#!/usr/bin/env python3

import math
import turtle


DISTANCE = 5
(tgt_x, tgt_y) = (0, 0)


def get_tgt_heading(from_x, from_y, to_x, to_y):
    dx = to_x - from_x
    dy = to_y - from_y
    if dx == 0:
        if dy > 0:
            return 90
        elif dy < 0:
            return -90
        else:  # dy == 0:
            return 0
    else:
        slope = dy / dx
        rads = math.atan2(dy, dx)
        return rads2degs(rads)


def move_turtle_toward_target():
    (x, y) = turtle.position()
    if (x, y) != (tgt_x, tgt_y):
        degs = get_tgt_heading(x, y, tgt_x, tgt_y)
        setheading(degs)
        forward(DISTANCE)


def rads2degs(rads):
    return rads * 180 / math.pi


def set_tgt(x, y):
    (tgt_x, tgt_y) =  (x, y)


if __name__ == '__main__':
    wn = turtle.Screen()
    # wn.onscreenclick(set_tgt)
    # turtle.listen()
    while True:
        move_turtle_toward_target()
