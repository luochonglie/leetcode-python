import unittest

from leetcode import palindrome_number as pn


class TestPalindromeNumberFinder(unittest.TestCase):

    def test_is_palindrome(self):
        expected = True
        actual = pn.is_palindrome(121)
        self.assertEqual(actual, expected)

        expected = False
        actual = pn.is_palindrome(-10)
        self.assertEqual(actual, expected)

        expected = True
        actual = pn.is_palindrome(0)
        self.assertEqual(actual, expected)

        expected = True
        actual = pn.is_palindrome(11)
        self.assertEqual(actual, expected)


