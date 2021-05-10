""" Lab 2.1 Python Development Exercises
You need to create two functions to substitute str() and int(). A function
called int_to_str() that converts integers into strings and a function called
str_to_int() that converts strings into integers.

Examples:
int_to_str(4) ➞ "4"
str_to_int("4") ➞ 4
int_to_str(29348) ➞ "29348"

:authors: - Hugo Rodríguez
"""

import math
from utils import require


def digit_count(number: int) -> int:
    if number > 0:
        return int(math.log10(number)) + 1
    elif number < 0:
        return int(math.log10(-number)) + 1

    return 1


def digit(number: int, pos: int) -> int:
    return number // 10 ** pos % 10


def int_to_str(number: int) -> str:
    require(number is not None, "Expected an integer, 'None' given")
    require(
        isinstance(number, int),
        f"Expected an integer, '{type(number).__name__}' given"
    )

    str_num = ''
    digits = digit_count(number)
    for i in range(0, digits):
        str_num = chr(ord('0') + digit(abs(number), i)) + str_num

    return str_num if number >= 0 else '-' + str_num


def str_to_int(number: str) -> int:
    require(number is not None, "Expected a string, 'None' given")
    require(
        isinstance(number, str),
        f"Expected a string, '{type(number).__name__}' given"
    )
    require(
        number.lstrip("-+").isdigit(),
        f"Given string does not contain an integer, '{number}' given"
    )

    num = number.lstrip("-+")
    int_num = 0
    for i, char_dig in enumerate(num):
        int_num += (ord(char_dig) - ord('0')) * 10 ** (len(num) - i - 1)

    return int_num if not number.startswith('-') else int_num * -1
