# Exercize 1, Conditional Basics
# prompt the user for a day of the week, print out whether the day is Monday or not
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# create variables and make up values for the number of hours worked in one week
# the hourly rate how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
number_of_hours_per_week = -1
hourly_rate = -1
while number_of_hours_per_week < 1 or number_of_hours_per_week > 150:
    number_of_hours_per_week = int(input('How many hours did you work this week (1-150)?'))

while hourly_rate < 1 or hourly_rate > 2000:
    hourly_rate = int(input('How much do you make an hour?'))
# - how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time
# and a half if you work more than 40 hours
if number_of_hours_per_week > 40:
    paycheck = ((number_of_hours_per_week - 40) * (1.5 * hourly_rate)) + (40 * hourly_rate)
else:
    paycheck = (40 * hourly_rate)

print('You paycheck will be ', paycheck)

# ------------------------------------------
# Exercize 2a, Loop Basics
# While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:   5,6,7,8,9,10,11,12,13,14,15
# -------
# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# Alter your loop to count backwards by 5's from 100 to -10.
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
# Write a loop that uses print to create the output shown below.

print(' Loop while 15')
i = int(5)
while i <= 15:
    print(i)
    i += 1
#
print(' Loop while 100 - even numbers')
i = int(0)
while i <= 100:
    print(i)
    i += 2
#
print(' Loop backwards from 100 by 5')
i = int(100)
while i >= -10:
    print(i)
    i -= 5
#
print(' Loop squared numbers to 1,000,000')
i = int(2)
while i <= 1000000:
    i = i*i
    print(str(i))

#
print(' Loop backwards from 100 by 5, break out at 5')
i = int(100)
while i >= -10:
    print(i)
    if i == 5:
        break
    else:    
        i -= 5

# ------------------------------------------
# Exercize 2b, For Loops       
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
mult_table_num = 0
while mult_table_num <= 0:
    mult_table_num = int(input('Please input a valid number to start the multiplication table: '))

for x in range(1,11):
    print(f'{mult_table_num} x {x} = {mult_table_num*x}')

# Exercise 2 b ii
# #    Create a for loop that uses print to create the output shown below.
# 1, 22, 333, 4444, 55555,......  999999999
for x in range(1,10):
    num_str = str(x)
    print(num_str * x)

# ---------------------
# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
#   (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
#  Your output should look like this:
#  Number to skip is: 27
#  Here is an odd number: 1
#  Here is an odd number: 3
#  Here is an odd number: 5

odd_number = 51
while odd_number < 1 or odd_number > 50:
    input_number = input('Please input an odd number between 1 and 50: ')
    if input_number.isdigit():
        if int(input_number)%2 != 0:
            odd_number = int(input_number)
    else:
        odd_number = 0
for x in range(1,51):
    if x%2 != 0:
        if x == odd_number:
            print('Yikes! Skipping number: ',int(x)  )
        else:
            print('Here is an odd number:  ',int(x)  ) 

# ---------------------
# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)
pos_number = -1
while pos_number < 1: 
    input_number = input('Please input a positive number: ')
    if input_number.isdigit():
        if int(input_number) > 0:
            pos_number = int(input_number)
    else:
        pos_number = -1
for x in range(0,pos_number + 1):
    print('Printing numbers ',int(x)  )


# -------------------------------------------------------
#   Write a program that prompts the user for a positive integer. 
#   Next write a loop that prints out the numbers from the number the user entered down to 1.
pos_number = -1
while pos_number < 1: 
    input_number = input('Please input a positive number: ')
    if input_number.isdigit():
        if int(input_number) > 0:
            pos_number = int(input_number)
    else:
        pos_number = -1

for x in range(pos_number,0,-1):
    print('Printing numbers ',int(x)  )


# ------------------------------------------
# Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".