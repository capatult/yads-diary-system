import pytest
from lib.snippets import *


def test_make_snippet_returns_empty_string_if_argument_string_empty():
    result = make_snippet("")
    assert result == ""

def test_make_snippet_returns_one_word_argument():
    result = make_snippet("Greetings")
    assert result == "Greetings"

def test_make_snippet_returns_five_word_argument():
    result = make_snippet("Greetings, inhabitants of planet Earth!")
    assert result == "Greetings, inhabitants of planet Earth!"

def test_make_snippet_truncates_many_word_argument_and_appends_ellipsis():
    result = make_snippet("The quick brown fox jumped over the lazy dog.")
    assert result == "The quick brown fox jumped..."


def test_count_zero_words_in_empty_string():
    result = count_words("")
    assert result == 0

def test_count_one_word_in_string():
    result = count_words("aeiou")
    assert result == 1

def test_count_correct_number_of_words():
    result = count_words("Lorem ipsum dolor sit amet")
    assert result == 5

def test_only_whitespace_delineates_words():
    result = count_words("alpha-beta_gamma.delta epsilon\nzeta")
    assert result == 3

