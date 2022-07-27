import re as regular_expression

class StringValidation:
    def __init__(self, input_string):
        self.input_string = input_string

    def string_starts_with_capital(self, input_string):
        if input_string[0].isupper():
            return True
        else:
            return False

    def string_has_even_quotation(self, input_string):
        number_of_quotes = input_string.count('"')
        if number_of_quotes == 0:
            return True
        elif number_of_quotes % 2 == 0:
            return True
        else:
            return False 

    def string_termination_character(self, input_string):
        last_character_of_string = input_string[-1]
        valid_string_termination_character = [".", "?", "!"]
        if last_character_of_string in valid_string_termination_character:
            return True
        else:
            return False

    def string_has_single_peroid(self, input_string):
        if "." in input_string[:-1]:
            return False
        else:
            return True
        
    def string_numbers_are_spelt(self, input_string):
        for word in input_string.split():
            if word.isdigit():
                if int(word) < 13:
                    print(word)




if __name__ == "__main__":
    test_validation = StringValidation('The quick brown fox said “hello Mr lazy dog”.')
    print(test_validation.string_numbers_are_spelt('One lazy dog is too few, 12 is too many.'))
    