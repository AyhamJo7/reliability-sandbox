import unittest

from ops_pow import power


class PowerTest(unittest.TestCase):
    def test_power(self) -> None:
        self.assertEqual(power(6, 3), 216)


if __name__ == "__main__":
    unittest.main()
