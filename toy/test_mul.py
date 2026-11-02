import unittest

from mul import mul


class MulTests(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)


if __name__ == "__main__":
    unittest.main()
