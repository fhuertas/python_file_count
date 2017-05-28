import sys
import unittest

from file_count.utils import math


class TestMath(unittest.TestCase):
    def test_classic_mean(self):
        numbers = [10, 20, 30, 40, 50, 60]
        mean = 35
        mean_result = math.classic_mean(numbers)
        self.assertEqual(mean, mean_result)

    def test_mean_accumulated(self):
        numbers = [10, 20, 30, 40, 50, 60]
        new_value = 50
        prev_mean = math.classic_mean(numbers)
        numbers.append(new_value)
        expected_mean = math.classic_mean(numbers)
        mean = math.mean_accumulated(new_value, prev_mean, 6)
        self.assertEqual(expected_mean, mean)

    # Skipped because is very slow
    def test_mean_accumulated_big_data(self):
        count = int(sys.maxsize / 10000000000)

        mean = 0
        expected_mean = (count - 1) / 2
        for i in range(count):
            mean = math.mean_accumulated(i, mean, i)

        self.assertEqual(mean, expected_mean)
