from cmath import exp
from re import T
import unittest
from unittest import TestCase
from valid_string import StringValidation


string_validation_input_test_cases = ([
    # Invalid Test Cases
    ['The quick brown fox said "hello Mr. lazy dog".', False], 
    ['the quick brown fox said “hello Mr lazy dog".', False],
    ['"The quick brown fox said “hello Mr lazy dog."', False],
    ['One lazy dog is too few, 12 is too many.', False],
    ['Are there 11, 12, or 13 lazy dogs?', False],
    ['There is no punctuation in this sentence', False],
    # Valid Test Cases
    ['The quick brown fox said “hello Mr lazy dog”.', True],
    ['The quick brown fox said hello Mr lazy dog.', True],
    ['One lazy dog is too few, 13 is too many.', True], 
    ['One lazy dog is too few, thirteen is too many.', True], 
    ['How many "lazy dogs" are there?', True],
])


class TestStringMethods(unittest.TestCase):

    def test_string_starts_with_capital(self ):
        for input_string, expected in string_validation_input_test_cases:
            result = StringValidation.validate_string(input_string)
            self.assertEqual(result, expected)

    # def test_string_numbers_are_spelt(self):
    #     input_string = StringValidation.validate_string(r'One lazy dog is too few, 12 is too many.')
    #     self.assertFalse(input_string.string_numbers_are_spelt(), False)
    #     self.assertFalse(input_string.string_numbers_are_spelt(), False)




if __name__ == '__main__':
    unittest.main()