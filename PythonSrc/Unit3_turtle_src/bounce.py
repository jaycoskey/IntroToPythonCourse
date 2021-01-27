#!/usr/bin/env python3
# Derived from the script Turtle Wall Bounce v3.py, by Bob O'Hara.

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.penup()
# t.hideturtle()
# t.fillcolor('green')
t.shape('circle')
t.pensize(4)
global x
global y

x = 12
y = -34
t.goto(x, y)

global left_wall
global right_wall
global bottom_wall
global top_wall

left_wall   = -150
right_wall  =  100
bottom_wall = -150 
top_wall    =  100

global dx
global dy

dx = 11
dy = 13

t.pendown()
t.showturtle()
t.speed(1)
while True:
    # global x
    # global y
    # global dx
    # global dy
    # print('L({0:.2f}), R({1:.2f}), T({2:.2f}), B({3:.2f})'
    #     .format(left_wall, right_wall, top_wall, bottom_wall))
    
    if x < left_wall or x > right_wall:
        if x < left_wall:
            t.fillcolor('red')
            t.pencolor('red')
        elif x > right_wall:
            t.fillcolor('green')
            t.pencolor('green')
        dx = -1 * dx
    if y < bottom_wall or y > top_wall:
        if y < bottom_wall:
            t.fillcolor('blue')
            t.pencolor('blue')
        elif y > top_wall:
            t.fillcolor('magenta')
            t.pencolor('magenta')
        dy = -1 * dy
    x = x + dx
    y = y + dy
    t.goto(x, y)

# mainloop()
