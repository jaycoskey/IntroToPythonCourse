#!/usr/bin/env python3

def pascal(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return pascal(row - 1, col - 1) + pascal(row - 1, col)


def print_pascal_row(row):
    cols = [pascal(row, col) for col in range(0, row + 1)]
    for col in range(0, len(cols)):
        print(cols[col], end='')
        if col < row:
            print(',', end='')
    print()


if __name__ == '__main__':
    for row in range(0, 7):
        print_pascal_row(row)
