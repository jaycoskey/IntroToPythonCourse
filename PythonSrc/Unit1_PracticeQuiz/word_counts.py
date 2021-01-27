#!/usr/bin/env python3

def get_word_count_a(s):
    num_words = 0
    is_in_word = False
    for letter in s:
        letter = letter.lower()
        if letter >= 'a' and letter <= 'z':
            if not is_in_word:
                num_words = num_words + 1
            is_in_word = False
        else:
            is_in_word = True
    return num_words


def get_word_count_b(line):
    word_count = 0
    is_word = True
    for character in line:
        character = character.lower()
        if character >= 'a' and character <= 'z':
            if not is_word:
                word_count += 1
            is_word = True
        else:
            is_word = False
    return word_count


def get_word_count_c(letters):
    num_words = 0
    is_within_word = False
    for letter in letters:
        if letter >= 'a' and letter <= 'z':
            if not is_within_word:
                num_words += 1
            is_within_word = True
        else:
            is_within_word = False
    return num_words


def get_word_count_d(s):
    word_count = 0
    is_in_word = True
    for char in s:
        if char >= 'a' and char <= 'z':
            if not is_in_word:
                word_count += 1
            is_in_word = False
        else:
            is_in_word = True
    return word_count


s = 'fruit flies like a banana '
print(get_word_count_a(s))
print(get_word_count_b(s))
print(get_word_count_c(s))
print(get_word_count_d(s))
