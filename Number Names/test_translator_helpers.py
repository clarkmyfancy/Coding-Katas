from translator_helpers import Helpers
import unittest


class TestTranslatorHelpers(unittest.TestCase):
    
    def test_should_ouput_5_when_given_number_with_5_digits(self):
        self.assertEqual(5, Helpers().number_of_digits(12340))
    
    def test_should_get_first_digit(self):
        self.assertEqual(3, Helpers().get_first_digit(34509006543))
        
    def test_should_be_able_to_left_shift_number(self):
        self.assertEqual(543, Helpers().left_shift(6543))

    def test_should_get_3_commas(self):
        one_trillion = 100000000000000
        self.assertEqual(4, Helpers().get_number_of_commas_in_number(one_trillion))
    
    def test_should_get_0_commas(self):
        self.assertEqual(0, Helpers().get_number_of_commas_in_number(123))
     

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
