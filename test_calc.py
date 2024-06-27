import unittest
from calc import multiply

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(1, 1), 2)


if __name__ == '__main__':
    unittest.main()


