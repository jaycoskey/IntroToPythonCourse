#!/usr/bin/env python3

import unittest


class MyClass(unittest.TestCase):
    def test_increment(self):
        x = 0
        x += 1
        self.assertEqual(x, 1)
    def test_decrement(self):
        x = 0
        x -= 1
        self.assertEqual(x, -1)


if __name__ == '__main__':
    unittest.main()
