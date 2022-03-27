#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def is_palindrome_v1(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    revent = 0
    while revent < x:
        revent = revent * 10 + x % 10
        x //= 10

    return revent == x or revent // 10 == x
