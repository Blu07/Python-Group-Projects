# FUNCTION TO PRINT AN ITERABLE OBJECT IN A HUMAN-READABLE WAY

# Find the longest keyword in an iterable object (iterable_object) and return that length
def get_longest_keyword_length(iterable_object):
    """
  Return the length of the longest key in a dictionary.

  Args:
    iterable_object (dict): The dictionary to search for the longest key.

  Returns:
    int: The length of the longest key in the dictionary.
  """

    longest = 0
    for key in iterable_object.keys():
        # Iterate over each key in iterable-object, store the length of the longest key
        longest = len(key) if len(key) > longest else longest

    return longest


# Main Function to print an iterable object
def print_iterable(iterable_object, indentation=0):
    """
  Print an iterable object with indentation in a human-readable way.

  Args:
    iterable_object (list, set, tuple, dict): The iterable to print.
    indentation (int, optional): The number of spaces to indent by. Defaults to 0.
  """

    # Iterate through a DICTIONARY
    if isinstance(iterable_object, dict):
        max_key_length = get_longest_keyword_length(iterable_object)

        # Print each key-value pair in the dictionary with proper indentation and spacing before the value in order
        # to get a consistent indentation. If the value is an iterable:
        # recursively run the main function print_iterable() with that value as iterable_object.
        for key, value in iterable_object.items():
            if not isinstance(value, (dict, list, tuple, set)):
                print(
                    f"{' ' * indentation}{key}:{' ' * (max_key_length - len(key))} {value}"
                )  # This adds two spaces more than the variable 'max_key_length', which is important to remember

            else:
                print(f"{' ' * indentation}{key}:")
                print_iterable(
                    value, indentation + max_key_length + 2
                )  # +2: Remember to add two spaces more for an extra indent to be correct

    # Iterate through a LIST, SET or TUPLE
    elif isinstance(iterable_object, (list, tuple, set)):
        # Sets can not be iterated through, so turn it into a list
        if isinstance(iterable_object, set):
            iterable_object = list(iterable_object)

        # Print each value in the iterable with proper indentation. If the value is an iterable:
        # recursively run the main function print_iterable() with that value as iterable_object.
        for value in iterable_object:
            if not isinstance(value, (dict, list, tuple, set)):
                print(f"{' ' * indentation}{value}")

            else:
                print_iterable(value, indentation)

    # When an iterable not accounted for by the above if-statements gets passed
    else:
        raise TypeError(f"Unsupported iterable: {type(iterable_object)}")


if __name__ == "__main__":
    # Example iterable
    user = {
        'age': 24,
        'username': "StarFight",
        'inventory': {
            "weapons": ["Katana", "Boomerang"],
            "jewels": ["Emerald", "Ruby"],
            "bombs": 3,
            "spears": 4,
        },
        'is_active': False,
        'clan': "The Cushions",
    }
    data = {
        'name':
            'John Doe',
        'age':
            42,
        'email':
            'johndoe@example.com',
        'address': {
            'street': '123 Main St',
            'city': 'Any-town',
            'state': 'CA',
            'zip': '12345'
        },
        'numbers': [{
            'type': 'home',
            'number': '555-1234'
        }, {
            'type': 'work',
            'number': '555-5678'
        }],
        'is_active':
            True,
        'friends': [{
            'name':
                'Jane Smith',
            'age':
                35,
            'email':
                'janesmith@example.com',
            'address': {
                'street': '456 Oak St',
                'city': 'Any-town',
                'state': 'CA',
                'zip': '12345'
            },
            'numbers': [{
                'type': 'home',
                'number': '555-4321'
            }, {
                'type': 'work',
                'number': '555-8765'
            }],
            'is_active':
                False
        }, {
            'name':
                'Bob Johnson',
            'age':
                50,
            'email':
                'bobjohnson@example.com',
            'address': {
                'street': '789 Pine St',
                'city': 'Any-town',
                'state': 'CA',
                'zip': '12345'
            },
            'numbers': [{
                'type': 'home',
                'number': '555-1111'
            }, {
                'type': 'work',
                'number': '555-2222'
            }],
            'is_active':
                True
        }]
    }

    # Before vs. after
    print(f"Before:\n{data}\n\n\nAfter:\n")
    # Call Main function
    print_iterable(data)
