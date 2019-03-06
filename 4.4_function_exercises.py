# Define a function named is_two. 
# It should accept one input and return True if the passed input is either 
#    the number or the string 2 
#   False otherwise.
# ------
def is_two(passed_input):
    return_value = False
    if passed_input in ['two',2,'Two','TWO',2.0,'2']:
        return_value = True
    return return_value    
x = is_two('2')
print(x)

#  alternate way to do this,  figure out how to return the 'type' of a variable and act on it
##   this is the same as using isdigit(), but may need to interrogate more than just numeric or mot
def is_two(passed_input):
    return_value = False
    if type(passed_input) is int:        #  return the type,   use IS, not = for comparison
        if passed_value == 2:
            return_value = true
    elif type(passed_input) is float:
        if passed_value == 2.0:
            return_value = true
    else:         #  assume it is a string
        lower_input_value = passed_value.lower()
        if lower_input_value in ('two', '2',):
            return_value = true
    return return_value

x = is_two('2')
print(x)
