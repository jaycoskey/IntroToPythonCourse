#!/usr/bin/env python3

def print_truth_table_row(a, b, f):
    print('{0:5s}  {1:5s}  {2:5s}'.format(str(a), str(b), str(f(a, b))))


def print_truth_table(f):
    print_truth_table_row(False, False, f)
    print_truth_table_row(False, True,  f)
    print_truth_table_row(True,  False, f)
    print_truth_table_row(True,  True,  f)


def xor1(a, b):
    if a == False and b == False or a == True and b == True:
        return False
    else:
        return True


def xor2(a, b):
    return a != b


print_truth_table(xor1)
print()
print_truth_table(xor2)
