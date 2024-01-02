import unittest
from calculator import calculate_sum


class TestCalculator(unittest.TestCase):
    def test_sum_positive_numbers(self):
        result = calculate_sum(1, 2)
        self.assertEqual(result, 3)

    def test_sum_negative_numbers(self):
        result = calculate_sum(-3, -7)
        self.assertEqual(result, -10)

    def test_sum_mixed_numbers(self):
        result = calculate_sum(5, -2)
        self.assertEqual(result, 3)

    def test_sum_zero(self):
        result = calculate_sum(0, 8)
        self.assertEqual(result, 8)

    def test_sum_both_zeros(self):
        result = calculate_sum(0, 0)
        self.assertEqual(result, 0)
