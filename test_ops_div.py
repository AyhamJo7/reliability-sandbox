import unittest

from ops_div import divide


class DivideTest(unittest.TestCase):
    def test_divide(self) -> None:
        self.assertEqual(divide(6, 3), 2)


if __name__ == "__main__":
    unittest.main()
