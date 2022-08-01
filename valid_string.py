from curses.ascii import FS, isdigit
import re as regular_expression

class StringValidation:
    def __init__(self, input_string):
        self.input_string = input_string
        print(type(input_string))
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
        
<<<<<<< HEAD
    def string_numbers_are_spelt(self):
        invalid = regular_expression.findall(r"\b([1-9]|1[0-2])\b", self.input_string)
        if invalid:
            return False
        else:
            return True

if __name__ == "__main__":
    test_validation = StringValidation('The quick brown fox said “hello Mr lazy dog”.')
    validation_rule_for_input_string = test_validation.string_starts_with_capital() and test_validation.string_has_even_quotation() and test_validation.string_termination_character() and test_validation.string_has_single_peroid() and test_validation.string_numbers_are_spelt()
    if validation_rule_for_input_string:
        print('Input String is a valid string.')
    else:
        print('Input String is not a valid string.')
=======
    def string_numbers_are_spelt(self, input_string):
        number_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen"]
        for word in input_string.split():
            if word.isdigit():
                if int(word) < 13:
                    return True

        
            if str(word) in number_list:
                return True
            else:
                return False


# Numbers below 13 are spelled out (”one”, “two”, "three”, etc…).




if __name__ == "__main__":
    test_validation = StringValidation('The quick brown fox said “hello Mr lazy dog”.')
    print(test_validation.string_numbers_are_spelt('One lazy dog is too few, 13 is too many.'))
    
>>>>>>> 7aca85addbad9685626fdb30146bab208bbb5392
