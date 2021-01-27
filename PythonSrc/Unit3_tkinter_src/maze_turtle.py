#!/usr/bin/env python3

import turtle


def draw_square(t, x, y, side_length, color):
    t.penup()
    coords = maze2screen(x, y)
    t.goto(coords[0], coords[1])
    t.pendown()
    t.begin_fill()
    t.color('black', color)
    for k in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()


def print_soln(soln):
    print('{0:s} @ [{1:s}]'.format(
        str(soln.node),
        ','.join([str(move) for move in soln.path]),
        soln.cost
        ))
 

SIDE_LENGTH = 20


def maze2screen(x, y):
    (base_x, base_y) = (-150, 150)
    return (base_x + SIDE_LENGTH*x, base_y - SIDE_LENGTH*y)

    
if __name__ == '__main__':
    layout = [ '###############'
             , '#S#   #       #'
             , '# # ### ### # #'
             , '# #   #   # # #'
             , '# ### # ### # #'
             , '#     #   # # #'
             , '# ### ### #   #'
             , '# #   #   ### #'
             , '# # ### # # # #'
             , '# #   # # # # #'
             , '# # # # #   # #'
             , '# # # # ##### #'
             , '#   #   #F    #'
             , '###############' ]

    (wn, t) = (turtle.Screen(), turtle.Turtle())
    t.speed(0)
    for line in layout:
        for character in line:
            print(character, end='')
        print()
    print()

    for i in range(0, len(layout)):
        line = layout[i]
        for j in range(0, len(line)):
            char = line[j]
            color = None
            if char == ' ':
                color = None
            elif char == '#':
                color = 'gray'
            elif char == 'S':
                pos_begin = (j, i)
                color = 'red'
            elif char == 'F':
                pos_end = (j, i)
                color = 'green'
            else:
                pass  # Unrecognized character
            if color != None:
                draw_square(t, j, i, SIDE_LENGTH, color)
            print(char, end='')
        print()
    print()

    U = 'U'
    D = 'D'
    L = 'L'
    R = 'R'

    moves = [D,D,D,D,R,R,R,R,D,D,L,L,D,D,R,R,D,D,D,R,R,
             U,U,U,U,U,R,R,U,U,L,L,U,U,U,U,R,R,R,R,D,D,D,D,D,
             R,R,D,D,D,D,D,D,L,L,L,L]
    pos_cur = maze2screen( pos_begin[0], pos_begin[1])
    pos_cur = (pos_cur[0] + SIDE_LENGTH/2, pos_cur[1] - SIDE_LENGTH/2)
    t.penup()
    t.goto(pos_cur[0], pos_cur[1])
    t.color('blue')
    t.pensize(5)
    t.pendown()
    for move in moves:
        if move == U: 
            pos_cur = (pos_cur[0], pos_cur[1] + SIDE_LENGTH)
            t.goto(pos_cur[0], pos_cur[1])
        if move == D: 
            pos_cur = (pos_cur[0], pos_cur[1] - SIDE_LENGTH)
            t.goto(pos_cur[0], pos_cur[1])
        if move == L: 
            pos_cur = (pos_cur[0] - SIDE_LENGTH, pos_cur[1])
            t.goto(pos_cur[0], pos_cur[1])
        if move == R: 
            pos_cur = (pos_cur[0] + SIDE_LENGTH, pos_cur[1])
            t.goto(pos_cur[0], pos_cur[1])

    wn.mainloop()
