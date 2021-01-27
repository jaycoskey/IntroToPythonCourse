#!/usr/bin/env python3

import random

def get_pi_estimate(sample_count):
    '''Use a Monte Carlo technique to approximate
    the area of the unit circle'''
    inside_circle_count = 0
    for _ in range(0, sample_count):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if x**2 + y**2 < 1:
            inside_circle_count += 1
    pi = 4 * inside_circle_count / sample_count
    return pi

def print_pi_estimate(sample_count):
    pi = get_pi_estimate(sample_count)
    print('Samples={0:d}: Estimate={1:f}'
        .format(sample_count, pi))

if __name__ == '__main__':
    print_pi_estimate(1)
    print_pi_estimate(10)
    print_pi_estimate(100)
    print_pi_estimate(1000)
    print_pi_estimate(10000)
    print_pi_estimate(100000)
