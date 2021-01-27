#!/usr/bin/env python3

def remove_comment_from_line(s):
    result = ''
    for c in s:
        if c == '#':
            break
        else:
            result += c
    return result


def get_lines_from_file(filename):
    lines = open(filename).readlines()
    # Remove new line from end of line
    lines = [line.rstrip() for line in lines]
    return lines


if __name__ == '__main__':
    for line in get_lines_from_file('commented.py'):
        print(remove_comment_from_line(line))
