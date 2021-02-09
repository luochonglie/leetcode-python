# -*- coding: utf-8 -*-

import unittest

from leetcode import monotone_increasing_digits as solution


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertEqual(0, solution.monotone_increasing_digits(0))
        self.assertEqual(19, solution.monotone_increasing_digits(21))
        self.assertEqual(123, solution.monotone_increasing_digits(123))
        self.assertEqual(999, solution.monotone_increasing_digits(1101))

    def test_range(self):
        for i in range(1, 10):
            print(i)


if __name__ == '__main__':
    unittest.main()
