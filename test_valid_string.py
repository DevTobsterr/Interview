import unittest
import valid_string


valid_input_test_cases = [
    r'The quick brown fox said “hello Mr lazy dog”.',
    r'The quick brown fox said hello Mr lazy dog.',
    r'One lazy dog is too few, 13 is too many.', 
    r'One lazy dog is too few, thirteen is too many.', 
    r'How many "lazy dogs" are there?'
]

invalid_input_test_cases = [
    r'The quick brown fox said "hello Mr. lazy dog".', 
    r'the quick brown fox said “hello Mr lazy dog".',
    r'"The quick brown fox said “hello Mr lazy dog."',
    r'One lazy dog is too few, 12 is too many.'
    r'Are there 11, 12, or 13 lazy dogs?'
    r'There is no punctuation in this sentence'
]

class TestStringMethods(unittest.TestCase):

    def test_string_starts_with_capital(self):
        for valid_input_test_case in valid_input_test_cases: 
            result = valid_string.StringValidation.string_starts_with_capital(self, valid_input_test_case)
            self.assertTrue(result)


    def test_string_starts_with_capital(self):
        for invalid_input_test_case in invalid_input_test_cases: 
            result = valid_string.StringValidation.string_starts_with_capital(self, invalid_input_test_case)
            self.assertFalse(result)




if __name__ == '__main__':
    unittest.main()