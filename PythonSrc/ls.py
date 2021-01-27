#!/usr/bin/env python3

import os


def list_files(directory='.'):
    items = os.listdir(directory)
    for item in items:
        if item == '.' or item == '..':
            next
        path = directory + os.sep + item
        if os.path.isdir(path):
            print('{0:s} is a directory'.format(path))
            list_files(path)
        elif os.path.isfile(path):
            print(path)
        else:
            pass  # Do nothing; Not directory or file 


if __name__ == '__main__':
    list_files()
