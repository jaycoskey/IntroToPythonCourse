#!/usr/bin/env python3

ppa = ['pen', 'pineapple', 'apple']

if __name__ == '__main__':
    for item in ppa:
        print(item)
        if item == 'apple':
            ppa.append('pen')
