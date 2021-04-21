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

from python_fail import int_to_str
from python_fail import str_to_int
import unittest


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
