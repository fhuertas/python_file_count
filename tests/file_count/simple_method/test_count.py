import unittest
import pkg_resources

from file_count.simple_method import count

min_csv_path = pkg_resources.resource_filename('tests', 'resources/minimum.csv')


class TestCount(unittest.TestCase):
    def test_count_lines(self):
        result = count.count_lines(min_csv_path)
