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

import unittest
import math

"""
Test Cases:

1 - [TTP] Zero and positive integers conversion to string
2 - [TTP] Negative integer conversion to string
3 - [TTP] Large integers conversion to string
4 - [TTF] Exception raised when types other than int given
5 - [TTF] Exception raised when None given instead of int
6 - [TTP] Stringified zero and positive integer conversion to integer
7 - [TTP] Stringified negative integer conversion to integer
8 - [TTF] Exception raised when string is not an integer
9 - [TTF] Exception raised when types other than string given
10 - [TTF] Exception raised when None given instead of string
"""


def checkArgument(expression: bool, errorMsg: str):
    if not expression:
        raise ValueError(errorMsg)


def digitCount(number: int) -> int:
    if number > 0:
        return int(math.log10(number)) + 1
    elif number < 0:
        return int(math.log10(-number)) + 1

    return 1


def digit(number: int, n: int) -> int:
    return number // 10 ** n % 10


def int_to_str(number: int) -> str:
    checkArgument(number is not None, "Expected an integer, 'None' given")
    checkArgument(
        isinstance(number, int),
        f"Expected an integer, '{type(number).__name__}' given"
    )

    strNum = ''
    digits = digitCount(number)
    for i in range(0, digits):
        strNum = chr(ord('0') + digit(abs(number), i)) + strNum

    return strNum if number >= 0 else '-' + strNum


def str_to_int(number: str) -> int:
    checkArgument(number is not None, "Expected a string, 'None' given")
    checkArgument(
        isinstance(number, str),
        f"Expected a string, '{type(number).__name__}' given"
    )
    checkArgument(
        number.lstrip("-+").isdigit(),
        f"Given string does not contain an integer, '{number}' given"
    )

    num = number.lstrip("-+")
    intNum = 0
    for i, c in enumerate(num):
        intNum += (ord(c) - ord('0')) * 10 ** (len(num) - i - 1)

    return intNum if not number.startswith('-') else intNum * -1


class ConversionTest(unittest.TestCase):
    def test_pass_zero_and_positive_ints_convert_to_string(self):
        self.assertEqual("1234", int_to_str(1234))
        self.assertEqual("0", int_to_str(0))

    def test_pass_negative_ints_convert_to_string(self):
        self.assertEqual("-1", int_to_str(-1))
        self.assertEqual("-7654", int_to_str(-7654))

    def test_pass_large_ints_convert_to_string(self):
        self.assertEqual("9876543210", int_to_str(9876543210))
        self.assertEqual("-9876543210", int_to_str(-9876543210))

    def test_fail_raise_exception_when_passed_arg_is_not_int(self):
        with self.assertRaises(ValueError):
            int_to_str(3.1415926)

    def test_fail_raise_exception_when_none_passed_instead_of_int(self):
        with self.assertRaises(ValueError):
            int_to_str(None)

    def test_pass_stringified_zero_and_positive_ints_convert_to_int(self):
        self.assertEqual(1234, str_to_int("1234"))
        self.assertEqual(0, str_to_int("0"))
        self.assertEqual(777, str_to_int("+777"))

    def test_pass_stringified_negative_ints_convert_to_int(self):
        self.assertEqual(-1, str_to_int("-1"))
        self.assertEqual(-7654, str_to_int("-7654"))

    def test_fail_raise_exception_when_str_not_an_int(self):
        with self.assertRaises(ValueError):
            str_to_int("-aB6T!")

    def test_fail_raise_exception_when_passed_arg_is_not_str(self):
        with self.assertRaises(ValueError):
            str_to_int(2.7182818)

    def test_fail_raise_exception_when_none_passed_instead_of_str(self):
        with self.assertRaises(ValueError):
            str_to_int(None)


if __name__ == "__main__":
    unittest.main()
