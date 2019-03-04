print('Good Morning Ada!')
i_like_coffee = True   # switch to False to test else
if i_like_coffee:
    print('I like coffee!')
else:
    print('Ok - lets have some tea')
# ---
pizza_reference = input('What kind of pizza do you like?')
if pizza_reference == 'pineapple and hot sauce':
    print('Wow - what a coincidence!')
#    spicy_level = int(input('How spicy would you like it? (1-5)'))
elif pizza_reference == 'pepperoni and chocolate':
    print('hmmm... ok')
elif pizza_reference == 'cheese':
    print('Plain cheese,  ok!')
else:
    print('Not my favorite, but lets order some!')
# -
print('Ok - Done ordering pizza')
# -----------------------------------
# 1. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_the_week = input('What day of the week is it?')
if day_of_the_week.lower() == 'monday' or day_of_the_week == 'mon':
    print('Happy Monday!')
else:
    print('At least its not Monday')

# 2. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekend_list = ['saturday', 'sat', 'sunday', 'sun']

if day_of_the_week.lower() in weekend_list:
    print('Great, its the weekend! ')
else:
    print('another workday')
# 3. create variables for
# - the number of hour worked in one week
# - the hourly rate

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
