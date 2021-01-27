#!/usr/bin/env python3

def print_toc_line(width, name, page_num):
    page_num = str(page_num)
    width = width - len(name) - len(page_num)
    print(name + ('.' * width) + page_num)


print_toc_line(50, 'Alligators', 1)
print_toc_line(50, 'Bears', 12)
print_toc_line(50, 'Yaks', 437)
print_toc_line(50, 'Zebras', 451)
