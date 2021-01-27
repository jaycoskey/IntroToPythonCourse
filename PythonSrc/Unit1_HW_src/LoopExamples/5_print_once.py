#!/usr/bin/python3

def print_once_v1(items):
    # Print each item, if we haven't seen it before
    for i in range(0, len(items)):
        have_seen_before = False
        for j in range(0, i):
            if items[j] == items[i]:
                have_seen_before = True
                break
        if not have_seen_before:
            print(items[i])


def print_once_v2(items):
    seen = []
    for item in items:
        if not(item in seen):  # This introduces the 'in' operator
            print(item, " ")
            seen.append(item)


if __name__ == '__main__':
    items = [1,2,3,3,2,1,4]
    print_once_v1(items)
    print()
    print_once_v2(items)
