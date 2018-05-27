import unittest
from .util import *


class UtilityMethods(unittest.TestCase):

    def setUp(self):
        self.test_record = {
            'appearances': '1269',
            'current': 'YES',
            'death1': 'YES',
            'death2': '',
            'death3': '',
            'death4': '',
            'death5': '',
            'full_reserve_avengers_intro': 'Sep-63',
            'gender': 'MALE',
            'honorary': 'Full',
            'name_alias': 'Henry Jonathan "Hank" Pym',
            'notes': 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n',
            'probationary_introl': '',
            'return1': 'NO',
            'return2': '',
            'return3': '',
            'return4': '',
            'return5': '',
            'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)',
            'year': '1963',
            'years_since_joining': '52'
        }
        test_class = Avenger(self.test_record)

    def data_is_dict(self):
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
