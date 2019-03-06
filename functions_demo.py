# demo function to get an integer from the user
def get_integer_input(custom_prompt):
    user_input = input(custom_prompt)
    if not user_input.isdigit():
        print('Error: {} is not an integer'.format(user_input))
        return get_integer_input(custom_prompt)     # recursive
    return int(user_input)

inputted_number = get_integer_input('Please enter an int: ')
