#!/usr/bin/python3

s = ' The quick brown fox  jumps  over the lazy dog '


def get_word_count(s):
    word_count = 0
    is_in_word = False
    for letter in s:
        letter = letter.lower()
        if letter >= 'a' and letter <= 'z':
            if not is_in_word:
                word_count += 1
            is_in_word = True
        else:
            is_in_word = False
    return word_count


print(get_word_count(s))
