import math

class Helpers:
    
    def number_of_digits(self, number):
        digits = 0
        while int(number) > 0:
            number /= 10
            digits += 1
        return digits
    
    def get_first_digit(self, number):
        shifter = math.pow(10, self.number_of_digits(number) - 1)
        return int(number / shifter)
    
    def left_shift(self, number):
        shift = math.pow(10, Helpers().number_of_digits(number) - 1)
        return number % shift

    def left_shift_by_1000(self, number):
        shift = math.pow(10, Helpers().number_of_digits(number) - 1)
        return 

    def get_number_of_commas_in_number(self, number):
        commas = 0

        number /= 1000
        while int(number) > 0:
            number /= 1000
            commas += 1
        return commas
