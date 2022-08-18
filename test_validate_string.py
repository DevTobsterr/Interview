from validate_string import StringValidation
import pytest

string_validation_test_cases = ("test_input_string, expected_outcome_of_test",
    [
        # Invalid Test Cases - Assert False
        ('The quick brown fox said "hello Mr. lazy dog".', False), 
        ('the quick brown fox said “hello Mr lazy dog".', False),
        ('"The quick brown fox said “hello Mr lazy dog."', False),
        ('One lazy dog is too few, 12 is too many.', False),
        ('Are there 11, 12, or 13 lazy dogs?', False),
        ('There is no punctuation in this sentence', False),

        # Valid Test Cases - Assert True
        ('The quick brown fox said “hello Mr lazy dog”.', True),
        ('The quick brown fox said hello Mr lazy dog.', True),
        ('One lazy dog is too few, 13 is too many.', True), 
        ('One lazy dog is too few, thirteen is too many.', True), 
        ('How many "lazy dogs" are there?', True)
    ]
)

@pytest.mark.parametrize(*string_validation_test_cases)
def test_string_has_even_quotation(test_input_string, expected_outcome_of_test):
    string_validation = StringValidation(test_input_string)
    assert string_validation.string_has_even_quotation() == expected_outcome_of_test


@pytest.mark.parametrize(*string_validation_test_cases)
def test_string_starts_with_capital(test_input_string, expected_outcome_of_test):
    string_validation = StringValidation(test_input_string)
    assert string_validation.string_starts_with_capital() == expected_outcome_of_test


@pytest.mark.parametrize(*string_validation_test_cases)
def test_string_termination_character(test_input_string, expected_outcome_of_test):
    string_validation = StringValidation(test_input_string)
    assert string_validation.string_termination_character() == expected_outcome_of_test

@pytest.mark.parametrize(*string_validation_test_cases)
def test_string_has_single_peroid(test_input_string, expected_outcome_of_test):
    string_validation = StringValidation(test_input_string)
    assert string_validation.string_has_single_peroid() == expected_outcome_of_test


@pytest.mark.parametrize(*string_validation_test_cases)
def test_string_numbers_are_spelt(test_input_string, expected_outcome_of_test):
    string_validation = StringValidation(test_input_string)
    assert string_validation.string_numbers_are_spelt() == expected_outcome_of_test

