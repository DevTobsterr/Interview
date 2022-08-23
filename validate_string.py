import re as regular_expression

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
class StringValidation:
    # Init class passing in input_string
    def __init__(self, input_string):
        self.input_string = input_string
        if type(input_string) in ["str"]:
            # Checking if input type is a string
            print("Input value is not String")
        else:
            pass

    def string_starts_with_capital(self):
        # Func splits chars and checks if the first letter is upper caase. 
        if self.input_string[0].isupper():
            return True
        else:
            return False

    def string_has_even_quotation(self):
        number_of_quotes = self.input_string.count('"')
        # Counts the number of " in the string
        if number_of_quotes == 0:
            return True
            # Check if 0 quotes are found resulting in a valid string
        elif number_of_quotes % 2 == 0:
            # Checks if there is a even number of quotes by diving the count by 2 and checking for remainder of 0
            return True
        else:
            return False 
            # Returning False if no condition is met.

    def string_termination_character(self):
        last_character_of_string = self.input_string[-1]
        # Using python slice to get the last char
        valid_string_termination_character = [".", "?", "!"]
        # Predefining acceptable termination chars
        if last_character_of_string in valid_string_termination_character:
            # Comparing the last string is a acceptable char
            return True
        else:
            return False

    def string_has_single_peroid(self):
        print(self.input_string[:-1])
        if "." in self.input_string[:-1]:
            # Checking if there is a . in string EXCLUDING the last char
            return False
        else:
            return True
        
    def string_numbers_are_spelt(self):
        invalid = regular_expression.findall(r"\b([1-9]|1[0-2])\b", self.input_string)
        # Using python regular expression to find all numbers under 13 and return false if found
        if invalid:
            return False
        else:
            return True


def main(input_string):
    if input_string != "":
        # Checking if input string is blank before moving on
        test_validation = StringValidation(input_string) 
        validation_rule_for_input_string = test_validation.string_starts_with_capital() \
            and test_validation.string_has_even_quotation() and test_validation.string_termination_character() \
                and test_validation.string_has_single_peroid() and test_validation.string_numbers_are_spelt()

        # Creating an Instance of the class and checking if all funcs return True to be a valid string
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


