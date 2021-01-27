#!/usr/bin/env python3

lines = open('/usr/share/dict/words').readlines()
for line in lines:
    line = line.rstrip()
    length = len(line)
    if len(line) < 2:
        continue 
    if line[0] == line[length - 2] and line[1] == line[length - 1]:
        print(line)
