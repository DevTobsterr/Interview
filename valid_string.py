import re as regular_expression

string_validation_input_test_cases = [
    # Invalid Test Cases
    r'The quick brown fox said "hello Mr. lazy dog".', 
    r'the quick brown fox said “hello Mr lazy dog".',
    r'"The quick brown fox said “hello Mr lazy dog."',
    r'One lazy dog is too few, 12 is too many.',
    r'Are there 11, 12, or 13 lazy dogs?',
    r'There is no punctuation in this sentence',
    # Valid Test Cases
    r'The quick brown fox said “hello Mr lazy dog”.',
    r'The quick brown fox said hello Mr lazy dog.',
    r'One lazy dog is too few, 13 is too many.', 
    r'One lazy dog is too few, thirteen is too many.', 
    r'How many "lazy dogs" are there?',
]

class StringValidation:
    def __init__(self, input_string):
        self.input_string = input_string
        if type(input_string) in ["str"]:
            print("Input value is not String")
        else:
            pass

    def string_starts_with_capital(self):
        if self.input_string[0].isupper():
            return True
        else:
            return False

    def string_has_even_quotation(self):
        number_of_quotes = self.input_string.count('"')
        if number_of_quotes == 0:
            return True
        elif number_of_quotes % 2 == 0:
            return True
        else:
            return False 

    def string_termination_character(self):
        last_character_of_string = self.input_string[-1]
        valid_string_termination_character = [".", "?", "!"]
        if last_character_of_string in valid_string_termination_character:
            return True
        else:
            return False

    def string_has_single_peroid(self):
        if "." in self.input_string[:-1]:
            return False
        else:
            return True
        

    def string_numbers_are_spelt(self):
        invalid = regular_expression.findall(r"\b([1-9]|1[0-2])\b", self.input_string)
        if invalid:
            return False
        else:
            return True

    def string_numbers_are_spelt(self):
        invalid = regular_expression.findall(r"\b([1-9]|1[0-2])\b", self.input_string)
        if invalid:
            return False
        else:
            return True

if __name__ == "__main__":
    for input_string in string_validation_input_test_cases:
        test_validation = StringValidation(input_string)
        validation_rule_for_input_string = test_validation.string_starts_with_capital() \
            and test_validation.string_has_even_quotation() and test_validation.string_termination_character() \
                and test_validation.string_has_single_peroid() and test_validation.string_numbers_are_spelt()





    

