#!/usr/bin/env python3
# Derived from the Simple Turtle Graphics Game, by Christian Thompson

# Bug (not from Thompson's code):
#     Turtle stops listening to events once reaching the target

import math
import turtle


(tgt_x, tgt_y) = (500, 0)


# Set up screen
wn = turtle.Screen()
wn.bgcolor('lightgreen')


# Create turtle
t = turtle.Turtle()
t.color('blue')
t.shape('triangle')
t.penup()
t.width(4)
t.speed(0)


# Set speed variable
speed = 1


def get_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx **2 + dy ** 2)

    
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


def move_turtle_toward_target(t, speed):
    (x, y) = t.position()
    if get_distance(x, y, tgt_x, tgt_y) > 10:
        degs = get_tgt_heading(x, y, tgt_x, tgt_y)
        t.setheading(degs)
        t.forward(speed)


def rads2degs(rads):
    return rads * 180 / math.pi


def set_tgt(x, y):
    global tgt_x
    global tgt_y
    (tgt_x, tgt_y) =  (x, y)
    print('Set target coordinates to ({0:f}, {1:f})'.format(x, y))


def speed_increase():
    global speed
    speed += 1


def speed_decrease():
    global speed
    speed -= 1


def speed_zero(x, y):
    global speed
    speed -= 1


def turn_left(t):
    t.left(30)


def turn_right(t):
    t.right(30)


# turtle.listen()
# turtle.onkey(lambda: turn_left(t), 'Left')
# turtle.onkey(lambda: turn_right(t), 'Right')
# turtle.onkey(speed_increase, 'Up')
# turtle.onkey(speed_decrease, 'Down')
wn.onscreenclick(set_tgt)
wn.listen()


print('INFO: About to enter turtle movement loop')
t.pendown()
while True:
    move_turtle_toward_target(t, speed) 
    # t.forward(speed)
