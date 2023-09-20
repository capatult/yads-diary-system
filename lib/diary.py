

# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

# Function signature:
#   * Name: estimate_reading_time
#   * Arguments: one string, `string`
#   * Return value(s): one integer, representing the estimate time in seconds to read 
#     (rounded to the nearest second)
#   * Side effect(s): no side effects

ESTIMATED_WORDS_PER_SECOND = 200 / 60

def estimate_reading_time(string):
    if not isinstance(string, str):
        raise Exception("Argument was not a string.")
    return round(len(string.split()) / ESTIMATED_WORDS_PER_SECOND + 0.5)






# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

# Function signature:
#   * Name: has_good_grammar
#   * Arguments: one string, `string`
#   * Return value(s): one boolean
#   * Side effect(s): no side effects

def has_good_grammar(string):
    pass




# As a user
# So that I can keep track of my tasks
# I want to check if a text includes the string #TODO.

# Function signature:
#   * Name: check_todo_present
#   * Arguments: one string, `string`
#   * Return value(s): one boolean
#   * Side effect(s): no side effects

def check_todo_present(string):
    # Me on my way to defy the duck typing principle:
    if not isinstance(string, str):
        raise Exception("Input must be a string!")
    result = "#TODO" in string
    return result
