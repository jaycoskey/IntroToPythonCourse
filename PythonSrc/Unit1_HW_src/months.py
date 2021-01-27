#!/usr/bin/env python3

months = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'
         , 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
         ]
m2days = { 'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30
         , 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31
         }
for m in range(0, len(months)):
    print('{0:s} -> {1:d}'.format(months[m], m2days[months[m]]))
