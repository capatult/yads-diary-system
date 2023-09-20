# Diary System Function Design Recipes

Function implementations are found in `./lib/diary.py`.

Function recipes are found in `./tests/test_diary.py`.

## Estimate reading time

### 1. Problem description

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

### 2. Function signature

```python

def estimate_reading_time(string):
    """Estimate the reading time of a string, assuming 200 words per minute reading speed

    Parameters:
        `string`: a string containing words the user might read

    Returns:
        One integer, representing estimated reading time in seconds, rounded up

    Side effects:
        This function doesn't have side effects
    """
    pass
```

See `./lib/diary.py` for the implementation of the function.

### 3. Examples for testing

```python
# EXAMPLE

"""
Given an empty string
It returns the integer 0
"""
estimate_reading_time("") => 0

"""
Given a string with 1 word
It returns the integer 1
"""
extract_uppercase("salutations") => []

"""
Given a string with words joined by punctuation and no whitespace
It returns the integer 1
"""
estimate_reading_time("this-will_all.be:interpreted#as?a;single,word") => 1

"""
Given a string with 200 words
It returns the integer 60
"""
estimate_reading_time(" ".join("something" for __ in range(200))) => 60

"""
Given a string with 10 words
It returns the integer 3
"""
estimate_reading_time("a b c d e; f g h i j;") => 3

"""
Given a string with 11 words
It returns the integer 4
"""
estimate_reading_time("a b c d e; f g h i j; k") => 4

"""
Given a None value
It throws an error
"""
estimate_reading_time(None) throws an error
```

### 4. Implementation of behaviour

See `./tests/test_diary.py` for the implementation of the tests.

## Check grammar of string

### 1. Problem description

> As a user
> So that I can improve my grammar
> I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

### 2. Function signature

```python

def has_good_grammar(text_to_check):
    """Check that a text follows certain grammatical principles:
    * it must start with a capital letter;
    * it must end with a suitable punctuation character.

    Parameters:
        `text_to_check`: a string containing text the user would like to grammar-check.

    Returns:
        One boolean, True if the string meets the grammatical criteria, False otherwise.

    Side effects:
        This function doesn't have side effects
    """
    pass
```

See `./lib/diary.py` for the implementation of the function.

### 3. Examples for testing

```python
# EXAMPLE

"""
Given an empty string
It returns the integer 0
"""
estimate_reading_time("") => 0

"""
Given a string with 1 word
It returns the integer 1
"""
extract_uppercase("salutations") => []

"""
Given a string with words joined by punctuation and no whitespace
It returns the integer 1
"""
estimate_reading_time("this-will_all.be:interpreted#as?a;single,word") => 1

"""
Given a string with 200 words
It returns the integer 60
"""
estimate_reading_time(" ".join("something" for __ in range(200))) => 60

"""
Given a string with 10 words
It returns the integer 3
"""
estimate_reading_time("a b c d e; f g h i j;") => 3

"""
Given a string with 11 words
It returns the integer 4
"""
estimate_reading_time("a b c d e; f g h i j; k") => 4

"""
Given a None value
It throws an error
"""
estimate_reading_time(None) throws an error
```

### 4. Implementation of behaviour

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

See `./tests/test_diary.py` for the implementation of the tests.








# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!