import pytest
from lib.check_todo_present import *

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
