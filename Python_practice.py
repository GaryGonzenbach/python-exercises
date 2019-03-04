#  create two arrays (lists) in a dictionary
#  first array is named movies, and contains the names of three movies
#  second array is named rental_days,  contains integers which is the number of days each movie was rented
#  , to practise manipulating this,  use a List Comprehension (instead) of a for loop to evalauate the cost
my_movies = {
    'movies': ['Little Mermaid', 'Brother Bear', 'Hercules'],
    'rental_days': [3, 5, 1]
}
# now,  assume that each rental is $3 per day, sum up the costs
#  here it it, using a List Comprehension

Movie_Cost = 3
Total_Movie_Cost = sum([n * Movie_Cost for n in my_movies['rental_days']])
#  this gives me a total dollars for each movie,  note that you can access the values in the 'rental_days' array by using the key,
#       'rental_days',    [9, 15, 3],  and sums it
print('Total Cost ' + str(Total_Movie_Cost))
#--------------------------------------------
company_rates = {'google': 400, 'amazon': 380, 'facebook': 350}
hours_worked = {'google': 6, 'amazon': 4, 'facebook': 10}

for company in hours_worked.keys:
    paycheck = hours_worked[company] * company_rates[company]
    print(f'I will get payed {paycheck} from {company} this week.')

#----------------------------------
class_is_full = False
schedule_has_conflicts = False
can_enroll = not class_is_full and not schedule_has_conflicts
print('Can_enroll = ', can_enroll)
#------------------------
n_items_bought = 4
offer_is_valid = True
is_premium_member = False
should_apply_discount = offer_is_valid and (n_items_bought > 2 or is_premium_member)
#-----------------------
username = 'codeup'
password = 'notastrongpassword'
Problem_statment = '''the password must be at least 5 characters
    the username must be no more than 20 characters
    the password must not be the same as the username
    bonus neither the username or password can start or end with whitespace'''

is_password_long_enough = len(password) >= 5
is_username_short_enough = len(username) <= 20
password_and_username_match = password == username
credentials_are_valid = is_password_long_enough and is_user_name_short_enough and not password_and_username_match
