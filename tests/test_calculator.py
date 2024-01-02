import unittest
from calculator import calculate_sum


class TestCalculator(unittest.TestCase):
    def test_calculate_cum(self):
        result = calculate_sum(1, 2)
        self.assertEqual(result, 3)
