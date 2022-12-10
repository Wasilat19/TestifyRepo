import unittest
import compare


class TestCompare(unittest.TestCase):
    def test_compare_strings(self):
        self.assertEqual(compare.compare_strings("Python", "Python"), True)

    def test_compare_numbers(self):
        self.assertEqual(compare.compare_numbers(5, 3), False)


if __name__ == '__main__':
    unittest.main()
