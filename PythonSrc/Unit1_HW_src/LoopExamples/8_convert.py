#!/usr/bin/python3

digit2char = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4'
             , 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'
             }


# Convert a positive integer (n) to a string
def int2str(n):
    assert(n > 0)
    result = ''
    while n > 0:
        digit = n % 10
        n = (n - digit) / 10
        result = digit2char[digit] + result
    return result


char2int = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4
           , '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
           }


# Convert a string representating an int > 0 to that int
def str2int(s):
    assert(len(s) > 0)
    result = 0
    for position in range(0, len(s)):
        digit = s[position]
        result = 10 * result + char2int[digit]
    return result


print(int2str(816357492))
print(str2int('816357492'))
