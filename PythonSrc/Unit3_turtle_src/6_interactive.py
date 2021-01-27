#!/usr/bin/env python3
# From www.dreamincode.net

import turtle


DISTANCE = 25
ANGLE = 30 


def go_forward(t): t.forward(DISTANCE)
def go_left(t): t.left(ANGLE)
def go_right(t): t.right(ANGLE)
def go_back(t): t.back(DISTANCE)


def quit(): screen.bye()


def setup_turtle_props(t, shape, size, width, col, x, y):
    t.up()
    t.shape(shape)
    t.turtlesize(size)
    t.color(col)
    t.width(width)
    t.goto(x, y)
    t.setheading(90)
    t.down()


def setup_turtle_keys(window, t, up, left, right, down):
    window.onkey(lambda: go_forward(t), up)
    window.onkey(lambda: go_left(t), left)
    window.onkey(lambda: go_right(t), right)
    window.onkey(lambda: go_back(t), down)


def main():
    wn = turtle.Screen()
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()

    setup_turtle_props(t1, 'turtle', 2, 2, 'blue', -200, 200)
    setup_turtle_props(t2, 'turtle', 2, 2, 'red',   200, 200)
    setup_turtle_keys(wn, t1, 'e', 's', 'f', 'c')
    setup_turtle_keys(wn, t2, 'i', 'j', 'l', 'm')
    setup_turtle_keys(wn, t2, 'Up', 'Left', 'Right', 'Down')

    wn.onkey(quit, 'Escape')
    wn.listen()
    wn.mainloop()


if __name__ == '__main__':
    main()
