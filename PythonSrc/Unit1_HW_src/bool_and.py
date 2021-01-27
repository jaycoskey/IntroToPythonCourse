#!/usr/bin/env python3

def bool_and(a, b):
    if a:
        return b
    else:
        return False        


def print_truth_row(a, b, f):
    print('{0:5s}  {1:5s}  {2:5s}'.format(str(a), str(b), str(f(a, b))))


if __name__ == '__main__':
    f = bool_and
    print_truth_row(False, False, f)
    print_truth_row(False, True,  f)
    print_truth_row(True,  False, f)
    print_truth_row(True,  True,  f)
