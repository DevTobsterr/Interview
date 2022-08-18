from valid_string import StringValidation

string_validation_input_test_cases = [
        # Invalid Test Cases
        r'The quick brown fox said "hello Mr. lazy dog".', 
        r'the quick brown fox said “hello Mr lazy dog".',
        r'"The quick brown fox said “hello Mr lazy dog."',
        r'One lazy dog is too few, 12 is too many.',
        r'Are there 11, 12, or 13 lazy dogs?',
        r'There is no punctuation in this sentence',
        r" ", 
        r"", 
        r"!£$%^&*()"

        # Valid Test Cases
        r'The quick brown fox said “hello Mr lazy dog”.',
        r'The quick brown fox said hello Mr lazy dog.',
        r'One lazy dog is too few, 13 is too many.', 
        r'One lazy dog is too few, thirteen is too many.', 
        r'How many "lazy dogs" are there?',
]

def main(input_string):
    if input_string != "":
        test_validation = StringValidation(input_string)
        validation_rule_for_input_string = test_validation.string_starts_with_capital() \
            and test_validation.string_has_even_quotation() and test_validation.string_termination_character() \
                and test_validation.string_has_single_peroid() and test_validation.string_numbers_are_spelt()

        if validation_rule_for_input_string:
            print(True)
            return True
        else:
            print(False)
            return False
    else:
        return False


if __name__ == "__main__":
    for input_string in string_validation_input_test_cases:
        main(input_string)




    