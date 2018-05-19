import unittest
from .util import *


class UtilityMethods(unittest.TestCase):

    def setUp(self):
        self.x = {'a': 1, 'b': 52, 'd': 6}
        self.y = ['a', 'c', 'd']
        self.validxy_val = 'a'
        self.invalidxy_val = 'g'
        self.valid_year_str = '1955'
        self.invalid_year_str = 'Not a Year'
        self.valid_month = 'Sep-55'
        self.invalid_month = 'Not a Month'
        self.vaid_date = datetime.date(1955, 9, 1)

    def test_int_is_int(self):
        is_int = to_int('11')
        self.assertTrue(type(is_int) == int)

    def test_float_str(self):
        is_int = to_int(11.5)
        self.assertTrue(type(is_int) == int)

    def test_invalid_str(self):
        self.assertIsNone(to_int("This Is Not an Int"))

    def test__int_list(self):
        is_int = to_int(['a', 'b', 'c'])
        self.assertFalse(type(is_int) == int)

    def test_int_empty(self):
        with self.assertRaises(TypeError):
            to_int()

    def test_gv_missing_arg(self):
        with self.assertRaises(TypeError):
            get_value(self.x)

    def test_gv_missing_dict_key(self):
        self.assertIsNone(get_value(self.x, self.invalidxy_val))

    def test_gv_missing_list_value(self):
        self.assertIsNone(get_value(self.y, self.invalidxy_val))

    def test_gv_valid_dic_key(self):
        self.assertTrue(get_value(self.x, self.validxy_val) == self.x[self.validxy_val])

    def test_gv_valid_list(self):
        self.assertTrue(self.y[get_value(self.y, self.validxy_val)] == self.validxy_val)

    def test_gdj_valid_ym(self):
        self.assertEqual(get_date_joined(self.valid_year_str,self.valid_month), self.vaid_date)

    def test_gdj_invalidm_valid_y(self):
        self.assertIsNone(get_date_joined(self.valid_year_str, self.invalid_month))

    def test_gdj_invalid_y_valid_m(self):
        self.assertIsNone(get_date_joined(self.invalid_year_str, self.valid_month))

    def test_gdj_invalid_ym(self):
        self.assertIsNone(get_date_joined(self.invalid_year_str, self.invalid_month))

    def test_gdj_invalid_args(self):
        with self.assertRaises(TypeError):
            get_date_joined(self.valid_year_str)

if __name__ == '__main__':
    unittest.main()
