import unittest
from .util import *


class UtilityMethods(unittest.TestCase):

    def test_int_is_int(self):
        is_int = to_int('11')
        self.assertTrue(type(is_int) == int)

    def test_float_str(self):
        is_int = to_int(11.5)
        self.assertTrue(type(is_int) == int)

    def test_invalid_str(self):
        is_int = to_int("This Is Not an Int")
        self.assertFalse(type(is_int) == int)

    def test_list(self):
        is_int = to_int(['a', 'b', 'c'])
        self.assertFalse(type(is_int) == int)


if __name__ == '__main__':
    unittest.main()
