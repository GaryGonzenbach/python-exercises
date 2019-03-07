# working with files exercise   
# Read the contents of your last exercise file into a variable.
#     Exercise 1.i   Print out every line in the file

from sys import exit
import os 
filepath = '/Users/garygonzenbach/OneDrive/Codeup_Classwork/python-exercises/'
filename = '4.5_import_exercises.py'
print('Reading file ({}) contents.....'.format(filename))
path_file_name = os.path.join(filepath,filename)
error_catch = getattr(__builtins__,'FileNotFoundError',IOError)
try:
    with open(path_file_name, "r") as file:
#    lines = file.read().split('\n')
        lines = file.readlines()
# Exercise 1.ii  Print out every line in the file, but add a line numbers
    for num, line in enumerate(lines, 1):
        print('{}: {}'.format(num, line)) 
except error_catch:
    print('File not found! (path: {} file: {})'.format(filepath,filename))

# Exercise 2  write some python code to create a grocery list
#   2.i,  create a variable named grocery_list.   List with elements of three items you need to by
#   2.ii,  create a function named make_grocery_list; writes the contents of grocery_list to a file: 'my_grocery_list.txt'
#   2.iii, create a function named show_grocery_list; shows each item on the grocery list
#   2.iv, create a function named buy_item.  Input and accepts the name of an item, removes it from the file if found. 

grocery_list = ['Captain Crunch', 'ribeye', 'bacon']