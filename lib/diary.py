# User story:
#   As a user
#   So that I can keep track of my tasks
#   I want to check if a text includes the string #TODO.

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
