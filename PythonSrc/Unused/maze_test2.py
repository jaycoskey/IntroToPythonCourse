#!/usr/bin/env python3

layout = []
row0 = [1,2,3]
row1 = [4,5,6]
row2 = [7,8,9]
layout.append(row0)
layout.append(row1)
layout.append(row2)
print('Len of layout is {0:d}'.format(len(layout)))

for row_num in range(0, len(layout)):
    for col_num in range(0, len(layout[row_num])):
       print(layout[row_num][col_num], end='')
    print()
