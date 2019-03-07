# Exercise 1
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
# x = is_two('2')
# print(x)
#
#  alternate way to do this,  figure out how to return the 'type' of a variable and act on it
##   this is the same as using isdigit(), but may need to interrogate more than just numeric or mot
def is_two(passed_input):
    return_value = False
    if type(passed_input) is int:        #  return the type,   use IS, not = for comparison
        if passed_input == 2:
            return_value = true
    elif type(passed_input) is float:
        if passed_input == 2.0:
            return_value = true
    else:         #  assume it is a string
        lower_input_value = passed_input.lower()
        if lower_input_value in ('two', '2',):
            return_value = true
    return return_value

x = is_two('2')
print(x)
# -------------------------------------------------------------------------------------
# Exercise 2
# Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.
def is_vowel(passed_input):
    return_value = False
    if passed_input.lower() in {'a','e','i','o','u'}:
        return_value = True
    return return_value

#  alternate solution
#  def  is_vowel(a_string):
#           return a_string in 'aeiou'      # return True if  a e i o or u  is in a_string

# ------------------------------------------------------------------------------------------    
# Exercise 3
# Define a function named is_consonant. 
def is_consonant(passed_input):
    return_value = False
    if not passed_input.isdigit():
        if passed_input.lower() not in {'a','e','i','o','u'}:
            return_value = True
    return return_value

# ---------------------    
# Exercise 4
# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word 
# if the word starts with a consonant.
def camel_word(passed_input):
    return_str = passed_input
    if not passed_input.isdigit():
        First_char = passed_input[0:1]
        if First_char.lower() not in {'a','e','i','o','u'}:
            return_str = First_char.capitalize() + passed_input[1:]
    return return_str        

#  alternate solution to finish,,,,, use a splat to break apart the word
def cap_in_consonant(word):
    first_letter, *rest_of_letters = word
    return first_letter.upper() + rest_of_letters.lower()     #  this will get an error right now

# -----------------------------------------------------    
# Exercise 5
# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def tip_amount(bill_total, tip_percent):
    return_tip = 0
    if type(bill_total) is float and type(tip_percent) is float:
        if 0 < tip_percent < 1:
            return_tip = bill_total * tip_percent 
    elif type(bill_total) is int and type(tip_percent) is float:
        if 0 < tip_percent < 1:
            return_tip = bill_total * tip_percent 
    return return_tip

# how_much = tip_amount(15.6,0.1)
# print(how_much)

# ---------------------    
# Exercise 6
# Define a function named apply_discount. It should accept 
# a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(original_price, discount_percent):
    return_price = original_price
    if type(original_price) is float and type(discount_percent) is float:
        if 0 < discount_percent < 1:
            return_price = original_price - (original_price * discount_percent) 
    elif if type(bill_total) is int and type(tip_percent) is float:
        if 0 < discount_percent < 1:
            return_price = original_price - (original_price * discount_percent)             
    return return_price

# ---------------------    
# Exercise 7
# Define a function named handle_commas. It should accept a string 
# that is a number that contains commas in it as input, 
# and return a number as output.
def handle_commas(input_str):
    comma_pos = 10
    no_commas = input_str
    while comma_pos >= 0:
        comma_pos = no_commas.find(',')
        if comma_pos > -1:
            no_commas = no_commas[0:comma_pos] + no_commas[comma_pos+1:]
    return(no_commas)        

#  alternate solution,   using string replace function
#     string_without_commas = a_string.replace(',','')

# test,   without_commas = handle_commas(',2345,45')


# ---------------------    
# Exercise 8
# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(input_grade):
        if input_grade.isdigit():
            grade = int(input_grade)
        else:
            grade = -1
        letter_grade = ''
        if grade >= 88:
            if grade >= 98:
              letter_grade = 'A+'
            else:  
                letter_grade = 'A'
        elif grade >= 80:
            if grade >= 86:
                letter_grade = 'B+'
            else:    
                letter_grade = 'B' 
        elif grade >= 67:
            if grade >= 78:
                letter_grade = 'C+'
            else:    
                letter_grade = 'C' 
        elif grade >= 60:
            if grade >= 68:
                letter_grade = 'D+'
            else:    
                letter_grade = 'D' 
        elif grade >= 0:
            letter_grade = 'F' 
        return letter_grade

# ---------------------    
# Exercise 9
# Define a function named remove_vowels that accepts a string 
# and returns a string with all the vowels removed.

def  remove_vowel(a_string):
    for vowel in 'aeiou':
        a_string = a_string.replace(vowel,'')
    return a_string

# ---------------------    
# Exercise 10
# Define a function named normalize_name. It should accept a string 
# and return a valid python identifier, that is:
#    anything that is not a valid python identifier should be removed
#    leading and trailing whitespace should be removed
#    everything should be lowercase
#    spaces should be replaced with underscores
#    for example:   Name will become name, First Name will become first_name, 
#    % Completed will become completed


LETTERS = '_abcdefghijklmnopqrstuvwxyz0123456789'    #  convention to make constants as all upper and put them outside functions

def normalize_name(a_string):
    a_string = a_string.strip().replace(' ','_').lower()  #  replace spaces with underscore and make it lower case
    valid_characters = []       #  could also set up as an empty string
    for character in a_string:
        if character in LETTERS:
            valid_characters.append(character) 
    return ''.join(valid_characters)   # join is a method to turn the elemets from a LIST to a STRING

# normalize_name('Name') == {}".format(normalize_name('Name')))
# normalize_name('First Name') == {}".format(normalize_name('First Name')))
# normalize_name('% Completed') == {}".format(normalize_name('% Completed')))

# ---------------------    
# Exercise 11
# Write a function named cumsum that accepts a list of numbers 
# and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsums(numbers):
    sums = [numbers[0]]
    for n in numbers[1:]:
        last_number = sums[-1]
        next_number = last_number + current_number
        sums.appends(next.number)

# print("cumsums([1,1,1] == %s" % cumsum([1,1,1]))
# print("cumsums([1,2,3] == %s" % cumsum([1,2,3]))
# print("cumsums([1,2,3,4] == %s" % cumsum([1,2,3,4]))

