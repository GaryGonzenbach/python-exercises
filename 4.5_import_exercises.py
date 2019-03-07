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
# --------------------------------------
# Use the load function from the json module to open this file, 
# it will produce a list of dictionaries. 
# Using this data, write some code that calculates 
# and outputs the following information:
# ----------------
import json
from pprint import pprint
with open('profiles.json') as f:
    profile_data = json.load(f)
#  print the total number of users
number_of_users = len(profile_data)
print('Total number users in  file profile: ',number_of_users)

for user in profile_data:
    user_id = user['_id']
    print(user_id)     # print the user id
#    print(user.keys()) # print all the keys for that user dictionary
    for user in 

#   resume right here... use the book / dictionary example from yesterdays exercise to evaluate the keys and find answers to problems.......

books = [
    {
        'title': 'Atlas Shrugged',
        'author': 'Ayn Rand',
        'genre': 'Philosopy'
    },
    {
        'title': 'Beautiful Evidence',
        'author': 'Edward Tufte',
        'genre': 'Visualizations'
    },
    {
        'title': 'Oh the places you\'ll go',
        'author': 'Dr. Seuss',
        'genre': 'Whimsy'
    }
]


for book in books:
    if genre_to_show not in book['genre']:
        continue
 
    print('---------------')        
    print('- title: %s' % book['title'])    
    print('- author: %s' % book['author'])
    print('- genre: %s' % book['genre'])







for 

# for users in profile.keys():
#    print(users)
#  pprint(data)

