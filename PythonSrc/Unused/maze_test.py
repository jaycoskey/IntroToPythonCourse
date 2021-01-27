#!/usr/bin/env python3

from collections import namedtuple
import copy
import sys

class MapContainer:
    def __init__(self):
        self.layout = []
        print('Type of self.layout is {0:s}'.format(str(type(self.layout))))
        row = [1,2,3,4,5]
        for row_num in range(0, 5):
            self.layout.append(row[::])

    def print(self):
        for row_num in range(0, 5):
            # print('Type of layout[row_num]={0:s}'.format(str(type(self.layout[row_num]))))
            # print('Type of items={0:s}'.format(str(type(items))))
            for col_num in range(0, len(self.layout[row_num])):
                print(self.layout[row_num][col_num], end='')
            print()

    def set_at(self, row_num, col_num, letter):
        self.layout[row_num][col_num] = letter

if __name__ == '__main__':
    mc = MapContainer()
    mc.print()
    print()
    mc.set_at(2, 2, 0)
    print()
    mc.print()
