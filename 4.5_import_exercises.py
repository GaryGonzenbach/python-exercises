import functions_exercises

# -----------------------
x = functions_exercises.is_two(10)
print(x)
new_price = functions_exercises.apply_discount(10.89,0.25)
print(new_price)
without_vowels = functions_exercises.remove_vowel('abracadabra')
print(without_vowels)
# ------------------------
import itertools
x = ['a','b','c','1','2','3']
y = [1,2,3]
z = ['a','b','c','d']
#  print(list(itertools.permutations(x,2)))
print(list(itertools.permutations('abcd',2)))
# ----- # profiles.json exercise ---------------------------------
# Use the load function from the json module to open this file, 
# it will produce a list of dictionaries. 
# Using this data, write some code that calculates 
# and outputs the following information:
#       Total number of users
#       Number of active users
#       Number of inactive users
#       Grand total of balances for all users
#       Average balance per user
#       User with the lowest balance
#       User with the highest balance
#       Most common favorite fruit
#       Least common favorite fruit
#       Total number of unread messages for all users


# ----------------
import json
from pprint import pprint

def money(number):
    number = number.strip('$')
    try:
        [num,dec]=number.rsplit('.')
        dec = int(dec)
        aside = str(dec)
        x = int('1'+'0'*len(aside))
        price = float(dec)/x
        num = num.replace(',','')
        num = int(num)
        price = num + price
    except:
        price = int(number)
    return price

with open('profiles.json') as f:
    profile_data = json.load(f)
#  print the total number of users---------------------------------------------
number_of_users = len(profile_data)
print('Total number users in  file profile: ',number_of_users)
grand_total_balance = 0
user_cnt = 0
act_user_cnt = 0
inact_user_cnt = 0
user_balance = 0
min_balance_amnt = 0
max_balance_amnt = 0
min_balance_user = ''
max_balance_user = ''
total_unread_msg = 0
grand_total_balance = 0
fruit_dictionary = {}
for user in profile_data:
    user_id = user['_id']
    user_cnt += 1
    user_balance_str = user['balance']
    user_balance = money(user_balance_str)
    grand_total_balance += user_balance
    ave_user_balance = grand_total_balance / user_cnt
    user_name = user['name']
    user_status = user['isActive']
    user_fruit = user['favoriteFruit']
    if user['favoriteFruit'] in fruit_dictionary.keys():
        fruit_dictionary[user_fruit] += 1
    else:
        fruit_dictionary[user_fruit] = 1
    if user_status == True:
        act_user_cnt += 1
    else:
        inact_user_cnt += 1  
    if min_balance_amnt == 0:
        min_balance_user = user_name
        min_balance_amnt = user_balance
    else:
        if user_balance < min_balance_amnt:
            min_balance_user = user_name
            min_balance_amnt = user_balance
    if max_balance_amnt == 0:
        max_balance_user = user_name
        max_balance_amnt = user_balance
    else:
        if user_balance > max_balance_amnt:
            max_balance_user = user_name
            max_balance_amnt = user_balance
#    print('User: ',user_name, ' Total balance=', grand_total_balance, ' Active user cnt = ', act_user_cnt, 'Inactive user_cnt= ', inact_user_cnt, 'Average balance per user: ', ave_user_balance)

print('\n')
print(' Total number of users: ', user_cnt)
print(' Number of Active users: ', act_user_cnt)    
print(' Number of In-Active users: ', inact_user_cnt)  
print(' Grand Total of user balances: ', grand_total_balance) 
print(' Average user balance: ', ave_user_balance)
print(' User with highest balance: ', max_balance_user, '  Balance = ', max_balance_amnt) 
print(' User with lowest balance: ', min_balance_user, '  Balance = ', min_balance_amnt)
print(fruit_dictionary)
