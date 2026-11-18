import unittest

from app import add_numbers, subtract_numbers, multiply_numbers


class TestApp(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 6)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 7), 7)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 2), 3)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(4, 3), 12)


if __name__ == "__main__":
    unittest.main()
