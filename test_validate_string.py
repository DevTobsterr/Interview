import pytest # Importing pytest for testing
from validate_string import main # Importing main func from validate_string.py


string_validation_test_cases = ("test_input_string, expected_outcome_of_test",
    [
        # Invalid Test Cases - Assert False - Provided in the Spec
        (f'The quick brown fox said "hello Mr. lazy dog".', False), 
        (f'the quick brown fox said “hello Mr lazy dog".', False),
        (f'"The quick brown fox said “hello Mr lazy dog."', False),
        (f'One lazy dog is too few, 12 is too many.', False),
        (f'Are there 11, 12, or 13 lazy dogs?', False),
        (f'There is no punctuation in this sentence', False),

        # Testing rare use cases - Null Values, White Spaces and Special Chars
        (f'', False),
        (f'!@£$%^&*()_+', False),
        (f'          ', False),

        # Valid Test Cases - Assert True - Provided in the Spec
        (f'The quick brown fox said “hello Mr lazy dog”.', True),
        (f'The quick brown fox said hello Mr lazy dog.', True),
        (f'One lazy dog is too few, 13 is too many.', True), 
        (f'One lazy dog is too few, thirteen is too many.', True), 
        (f'How many "lazy dogs" are there?', True)

        (f'!@£$%^&*()_+', False),
        
    ]
)

@pytest.mark.parametrize(*string_validation_test_cases)
def test_main_validate_string(test_input_string, expected_outcome_of_test):
    # Single Test for main() passing in test input string and expected outcome of test
    string_validation = main(test_input_string)
    assert string_validation == expected_outcome_of_test
    # Asserting that the actual outcome of test is equal to the expected outcome of test
