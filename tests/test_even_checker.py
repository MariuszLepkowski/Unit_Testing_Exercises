import unittest
from even_checker import is_even


class TestEvenChecker(unittest.TestCase):
    def test_is_even_positive(self):
        result = is_even(2)
        self.assertTrue(result)

    def test_is_even_negative(self):
        result = is_even(3)
        self.assertFalse(result)

    def test_is_even_zero(self):
        result = is_even(0)
        self.assertTrue(result)

    def test_is_even_negative_even(self):
        result = is_even(-4)
        self.assertTrue(result)

    def test_is_even_negative_odd(self):
        result = is_even(-7)
        self.assertFalse(result)