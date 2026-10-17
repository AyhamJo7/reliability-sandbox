import unittest

from ops_mul import multiply


class MultiplyTest(unittest.TestCase):
    def test_multiply(self) -> None:
        self.assertEqual(multiply(6, 3), 18)


if __name__ == "__main__":
    unittest.main()
