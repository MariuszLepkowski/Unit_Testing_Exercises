import unittest
from even_checker import is_even


class TestEvenChecker(unittest.TestCase):
    def test_is_even(self):
        result = is_even(2)
        self.assertTrue(result)