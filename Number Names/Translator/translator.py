import math

from translator_helpers import Helpers

class Translator:

    result = ""

    segment_suffixes = [
        "",
        "thousand",
        "million",
        "billion",
        "trillion",
        "quadrillion"
    ]

    def translate(self, number):

        if number == 0:
            result = "zero"
            return result

        original_number = number
        iteration = 0
        # segment = self.get_segment(number, iteration)
        current_number = self.get_segment(which_segment=iteration, number=number)
        self.result += self.translate_segment(current_number)

        current_magnitude_suffix = self.get_current_magnitude_suffix(number)
        self.result += " " + current_magnitude_suffix if current_magnitude_suffix != "" else ""

        number /= 1000
        iteration += 1

        while int(number) > 0 :
            current_number = self.get_segment(which_segment=iteration, number=original_number)
            current_segment = self.translate_segment(current_number)
            self.result += " " + current_segment if current_segment != "" else ""
            current_magnitude_suffix = self.get_current_magnitude_suffix(number)
            self.result += " " + current_magnitude_suffix if (current_magnitude_suffix != "") and (current_segment != "") else ""

            number /= 1000
            iteration += 1

        #     self.result += ""
        return self.result

    def translate_segment(self, number):
        result = ""

        if number == 0:
            result += ""
            return result
        
        elif Helpers().number_of_digits(number) == 3:
            result += self.translate_three_digits(number)
        
        elif Helpers().number_of_digits(number) == 2:
            result += self.translate_last_two_digits(number)
        
        elif self.is_a_single_digit(number):
            result += self.translate_single_digit(number)

        return result

    def get_segment(self, which_segment, number):
        commas = Helpers().get_number_of_commas_in_number(number)
        if commas == 0:
            return number
        number = (number / math.pow(1000, commas - which_segment)) % 1000
        
        return int(number)

    def there_are_commas_remaining(self, number):
        pass

    def get_current_magnitude_suffix(self, number):
        comma_replacements_with_context = {
            0: "",
            1: "thousand",
            2: "million",
            3: "billion",
            4: "trillion",
            5: "quadrillion"
        }

        commas = Helpers().get_number_of_commas_in_number(number)
        return comma_replacements_with_context[commas]
    
    def is_a_single_digit(self, number):
        return number >= 0 and number < 10
    
    def is_a_teen(self, number):
        return number >= 10 and number < 20
    
    def translate_single_digit(self, number):
        result = ""
        if number == 1:
            result = "one"
        elif number == 2:
            result = "two"
        elif number == 3:
            result = "three"
        elif number == 4:
            result = "four"
        elif number == 5:
            result = "five"
        elif number == 6:
            result = "six"
        elif number == 7:
            result = "seven"
        elif number == 8:
            result = "eight"
        elif number == 9:
            result = "nine"
        return result
    
    def translate_teens(self, number):
        result = ""
        
        if number == 10:
            result = "ten"
        elif number == 11:
            result = "eleven"
        elif number == 12:
            result = "twelve"
        elif number == 13:
            result = "thirteen"
        elif number == 14:
            result = "fourteen"
        elif number == 15:
            result = "fifteen"
        elif number == 16:
            result = "sixteen"
        elif number == 17:
            result = "seventeen"
        elif number == 18:
            result = "eighteen"
        elif number == 19:
            result = "nineteen"
        return result
    
    def translate_last_two_digits(self, number):
        # number is in form: Yx
        result = ''

        if self.is_a_teen(number):
            result += self.translate_teens(number)
            return result

        first_digit = int(number / 10) * 10
        result += self.translate_first_digit_of_two_digit_number(first_digit)
        
        second_digit = number % 10
        if second_digit != 0:
            result += ' '
        result += self.translate_single_digit(second_digit)
        
        return result
        
    def translate_first_digit_of_two_digit_number(self, number):
        result = ""
        if number == 20:
            result = "twenty"
        elif number == 30:
            result = "thirty"
        elif number == 40:
            result = "fourty"
        elif number == 50:
            result = "fifty"
        elif number == 60:
            result = "sixty"
        elif number == 70:
            result = "seventy"
        elif number == 80:
            result = "eighty"
        elif number == 90:
            result = "ninety"
        return result
    
    def translate_three_digits(self, number):
        result = ""
        
        result += self.translate_single_digit(Helpers().get_first_digit(number))
        result += ' hundred'
        number = Helpers().left_shift(number)
        
        if number != 0:
            result += ' '
        
        if self.is_a_teen(number):
            result += self.translate_teens(number)
        elif Helpers().number_of_digits(number) == 2:
            result += self.translate_last_two_digits(number)
        else:
            result += self.translate_single_digit(number)
        return result
