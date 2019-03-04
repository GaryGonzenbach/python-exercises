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
#

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
while i >= 1000000:
    i = i ** 2
    print(i)
