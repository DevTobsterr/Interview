from turtle import st
import unittest
import valid_string

string_validation_input_test_cases = [
    # Invalid Test Cases
    r'The quick brown fox said "hello Mr. lazy dog".', 
    r'the quick brown fox said “hello Mr lazy dog".',
    r'"The quick brown fox said “hello Mr lazy dog."',
    r'One lazy dog is too few, 12 is too many.'
    r'Are there 11, 12, or 13 lazy dogs?'
    # Valid Test Cases
    r'There is no punctuation in this sentence'
    r'The quick brown fox said “hello Mr lazy dog”.',
    r'The quick brown fox said hello Mr lazy dog.',
    r'One lazy dog is too few, 13 is too many.', 
    r'One lazy dog is too few, thirteen is too many.', 
    r'How many "lazy dogs" are there?'

]

class TestStringMethods(unittest.TestCase):

    def test_string_starts_with_capital(self):
        string_valdation = valid_string.StringValidation("")
        self.assertEqual(self, "" , True)



if __name__ == '__main__':
    unittest.main()