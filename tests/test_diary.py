import pytest
from lib.diary import *


"""
Given an empty string
It returns the integer 0
"""
def test_empty_string_returns_0_seconds():
    estimated_reading_time = estimate_reading_time("")
    assert estimated_reading_time == 0

"""
Given a string with 1 word
It returns the integer 1
"""
def test_1_word_string_returns_1_second():
    estimated_reading_time = estimate_reading_time("salutations")
    assert estimated_reading_time == 1

"""
Given a string with words joined by punctuation and no whitespace
It returns the integer 1
"""
def test_punctuation_not_interpreted_as_boundary_between_words():
    estimated_reading_time = estimate_reading_time(
        "this-will_all.be:interpreted#as?a;single,word"
    )
    assert estimated_reading_time == 1

"""
Given a string with 200 words
It returns the integer 60
"""
def test_200_word_string_returns_60_seconds():
    long_string = " ".join("blah" for __ in range(200))
    estimated_reading_time = estimate_reading_time(long_string)
    assert estimated_reading_time == 60

"""
Given a string with 10 words
It returns the integer 3
"""
def test_10_word_string_returns_3_seconds():
    estimated_reading_time = estimate_reading_time("a b c d e; f g h i j;")

"""
Given a string with 11 words
It returns the integer 4
"""
def test_11_word_string_returns_4_seconds():
    estimated_reading_time = estimate_reading_time("a b c d e; f g h i j; k")

"""
Given a None value
It throws an error
"""
def test_estimate_reading_time_raises_error_if_argument_is_none():
    with pytest.raises(Exception) as e:
        estimated_reading_time = estimate_reading_time(None)
    error_message = str(e.value)
    assert error_message == "Argument was not a string."





def test_return_false_for_empty_string():
    assert check_todo_present("") == False

def test_return_true_if_string_is_hash_todo():
    assert check_todo_present("#TODO") == True

def test_return_true_if_big_string_contains_hash_todo():
    test_string = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor#TODOut labore et dolore magna aliqua.
"""
    assert check_todo_present(test_string) == True

def test_return_false_if_big_string_does_not_contain_hash_todo():
    test_string = """
Sphinx of Black Quartz, Judge My Vow. †®´¥†¨ƒ¨¥†ƒ¨†ƒ©^¨¥
"""
    assert check_todo_present(test_string) == False

def test_raise_exception_if_type_not_string():
    test_not_string = ["#TODO", "but", "not", "a", "string"]
    with pytest.raises(Exception) as e:
        check_todo_present(test_not_string)
    error_message = str(e.value)
    assert error_message == "Input must be a string!"
