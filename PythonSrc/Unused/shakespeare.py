#!/usr/bin/env python3

from collections import Counter
import math
import os
import sys

ALPHA_ORDS = range(ord('a'), 1 + ord('z'))
ALPHA_LETTERS = [chr(ascii_code) for ascii_code in ALPHA_ORDS]

# E.g., get_path('ShakespearePlays', 'Hamlet.txt')
#           = 'ShakespearePlays/Hamlet.txt'
def get_path(dir, filename):
    return dir + os.sep + filename  # os.sep = slash or backslash

# E.g., paths['Hamlet.txt'] = Count('a':94284, 'b':14283, ... )
def get_fname2counter(dir):
    fname2counter = dict()    # Create empty dictionary
    fnames = os.listdir(dir)  # Get list of filenames in directory dir
    for fname in fnames:
        path = get_path(dir, fname)
        cntr = Counter()
        lines = open(path).readlines()
        for line in lines:
            cntr += Counter(line)
        fname2counter[fname] = cntr
    return fname2counter

def get_alpha_count_list(cntr):
    alpha_count_list = [cntr[letter] for letter in ALPHA_LETTERS]
    return alpha_count_list

def get_percentages(alpha_count_list):
    total = sum(alpha_count_list)
    percentages = [count / total for count in alpha_count_list]
    return percentages

def get_dist(percentages1, percentages2):
    assert(len(percentages1) == len(percentages2))
    distance = 0
    for i in range(0, len(percentages1)):
        distance += math.sqrt((percentages1[i] - percentages2[i]) ** 2)
    return distance


if __name__ == '__main__':
    # print('{0:s}'.format(ALPHA_LETTERS.__str__()))
    # sys.exit(0)

    fname2counter = get_fname2counter('../ShakespearePlays')
    fname2percentages = dict()

    plays_counter = Counter()
    for fname in fname2counter.keys():
        cntr = fname2counter[fname]
        plays_counter += cntr

        alpha_count_list = get_alpha_count_list(cntr)
        fname2percentages[fname] = get_percentages(alpha_count_list)

    plays_alpha_count_list = get_alpha_count_list(plays_counter)
    plays_percentages = get_percentages(plays_alpha_count_list)

    fname2dist = dict()
    for fname in fname2percentages.keys():
        fpercentages = fname2percentages[fname]
        fname2dist[fname] = get_dist(fpercentages, plays_percentages)

    for fname in sorted(fname2dist, key=lambda fn: fname2dist[fn]):
        print('Play={0:s}, dist={1:f}'.format(fname, fname2dist[fname]))
