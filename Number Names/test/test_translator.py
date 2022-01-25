from translator import Translator
import unittest


class TestTranslator(unittest.TestCase):

    def test_should_output_correct_names_for_digits_less_than_ten(self):
        expected_results = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
        }
        for key in expected_results:
            self.assertEqual(expected_results[key], Translator().translate(key))
            
    def test_should_ouput_correct_names_for_digits_between_10_and_20(self):
        expected_results = {
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
        }
        for key in expected_results:
            self.assertEqual(expected_results[key], Translator().translate(key))
            
    def test_should_translate_double_digits(self):
        expected_results = {
            20: "twenty",
            31: "thirty one",
            42: "fourty two",
            53: "fifty three",
            64: "sixty four",
            75: "seventy five",
            86: "eighty six",
            97: "ninety seven"
        }
        for key in expected_results:
            self.assertEqual(expected_results[key], Translator().translate(key))
                
    def test_should_translate_three_digit_numbers(self):
        expected_results = {
            400: "four hundred",
            310: "three hundred and ten",
            999: "nine hundred and ninety nine"
        }
        for key in expected_results:
            self.assertEqual(expected_results[key], Translator().translate(key))

    def test_should_give_correct_comma_phrase_suffix(self):
        suffixes = {
            100: "",
            1000: "thousand",
            1000000: "million",
            1000000000: "billion",
            1000000000000: "trillion",
            1000000000000000: "quadrillion"
        }
        for key in suffixes:
            self.assertEqual(suffixes[key], Translator().get_magnitude_suffix(key))

    def test_should_get_correct_segments(self):
        # read in the form: 123,456,789
        first = 0 # 123
        self.assertEqual(123, Translator().get_segment(which_segment=first, number=123456))
        self.assertEqual(324, Translator().get_segment(which_segment=first, number=324))

        second = 1 # 456
        self.assertEqual(456, Translator().get_segment(which_segment=second, number=123456))


    def test_should_output_first_segment_responses(self):
        self.assertEqual("one million", Translator().translate(1000000))
        self.assertEqual("four hundred and eighty seven billion", Translator().translate(487000000000))
        self.assertEqual("four hundred and eighty seven thousand two hundred and thirty", Translator().translate(487230))
        self.assertEqual("seven billion four hundred and ninety nine thousand one hundred and four", Translator().translate(7000499104))

        

        

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
