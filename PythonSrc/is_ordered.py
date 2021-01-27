#!/usr/bin/env python3


def is_ordered0(items):
    for k in range(0, len(items) - 1):
        if items[k] > items[k + 1]:
            return False
    return True            


def is_ordered1(items):
    init = items[0:len(items) - 1]  # All except the last item
    tail = items[1:len(items)]      # All except the first item
    assert(len(init) == len(tail))
    for k in range(0, len(init)):
        if init[k] > tail[k]:
            return False
    return True


def is_ordered2(items):
    init = items[0:len(items) - 1]  # All except the last item
    tail = items[1:len(items)]      # All except the first item
    pairs = zip(init, tail)
    for k in pairs:
        if k[0] > k[1]:
            return False
    return True


if __name__ == '__main__':
    items = [8,1,6,3,5,7,4,9,2]
    print(is_ordered0(items))
    print(is_ordered1(items))
    print(is_ordered2(items))

    print('----------')

    ordered = range(1, 10)
    print(is_ordered0(ordered))
    print(is_ordered1(ordered))
    print(is_ordered2(ordered))
