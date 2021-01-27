#!/usr/bin/env python3

from collections import Counter


# YES
def print_duplicated_a(items):
    print('a')
    cntr = Counter(items)
    for key in cntr.keys():
        if cntr[key] > 1:
            print('Found a duplicated item: ', key)


# NO.  Doesn't print out the items themselves: only True and False
def print_duplicated_b(items):
    print('b')
    for a in items:
        for b in items:
            print('Found a duplicated item: ', a == b) 


# YES
def print_duplicated_c(items):
    print('c')
    for i in range(0, len(items)):
        for j in range(0, i):
            if items[j] == items[i]:
                print('Found a duplicated item: ', items[i]) 
                break


# NO
def print_duplicated_d(items):
    print('d')
    for a in items:
        for b in items:
            if a == b:
                print('Found a duplicate', a)


# NO.  Can't take len(item)
def print_duplicates_e(items):
    pass
#    for item in items:
#        if len(item) > 1:
#            print('Found a duplicated item: ', item)


no_dupes = [1,2,3,4,5]
print('Tests with no duplicates:')
duplicated_a(no_dupes)
duplicated_b(no_dupes)
duplicated_c(no_dupes)
duplicated_d(no_dupes)
duplicated_e(no_dupes)


dupes = [1,2,1,2,4]
print('Tests with duplicates:')
duplicated_a(dupes)
duplicated_b(dupes)
duplicated_c(dupes)
duplicated_d(dupes)
duplicated_e(dupes)
