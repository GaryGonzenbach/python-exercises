import pandas as pd
import numpy as np

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']
students
student_number = list(range(1, len(students) + 1))
shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
side_of_classroom = np.random.choice(['left', 'right'], len(students))
favorite_number = np.random.randint(1, 11, len(students))
pd.DataFrame(dict(name=students,
    student_no=student_number,
    shoe_size=shoe_sizes,
    side=side_of_classroom,
    favorite_number=favorite_number))
df = pd.DataFrame(dict(name=students,
    student_no=student_number,
    shoe_size=shoe_sizes,
    side=side_of_classroom,
    favorite_number=favorite_number))
df
students = pd.DataFrame(dict(name=students,
    student_no=student_number,
    shoe_size=shoe_sizes,
    side=side_of_classroom,
    favorite_number=favorite_number))
students
type(students)
students.shape
students.columns
students.favorite_number
students
students.rename(columns={'student_no': 'id', 'name': 'student_name'})
students.rename(columns={'student_no': 'id', 'name': 'student_name'},
    inplace=True)
studens.shape
students.shape
students.rename
students
students[['shoe_size', 'side']]
just_shoes_and_sides = students[['shoe_size', 'side']]
students[['shoe_size', 'side']]
students[['side', 'shoe_size']]
students['side', 'shoe_size']
students[['side', 'shoe_size']]
type(students[['side', 'shoe_size']])
type(students[['side']])
type(students['side'])
students.head()
students.sample(5)
students.tail()
students[['favorite_number', 'name']]
students[['favorite_number', 'student_name']]
students[['favorite_number', 'student_name']].head()
students[['favorite_number', 'student_name']].sample(7)
names_and_numbers = students[['favorite_number', 'student_name']]
names_and_numbers.sample(7) 
# students[['favorite_number', 'student_name']].sample(7)
students.sample(7)[['favorite_number', 'student_name']]
students.sample(7)[['favorite_number', 'student_name']][['student_name', 'favorite_number']].head(3)
students.shoe_size
students.favorite_number
students.shoe_size / students.favorite_number
df['ss_to_fn'] = students.shoe_size / students.favorite_number
df
df
del df['ss_to_fn']
df
df
df.drop(columns=['name', 'student_no', 'shoe_size'])
df
df.assign(ss_to_fn=students.shoe_size / students.favorite_number)
df.assign(ss_to_fn=students.shoe_size / students.favorite_number).assign(ss_to_fn=students.shoe_size / students.favorite_number)
df.assign(favorite_number=df.favorite_number + 1)
(df.shoe_size - df.shoe_size.mean()) / df.shoe_size.std()
df['z_shoe_size'] = (df.shoe_size - df.shoe_size.mean()) / df.shoe_size.std()
df
df['z_shoe_size'] = [1, 2, 3]
df['z_shoe_size'] = (df.shoe_size - df.shoe_size.mean()) / df.shoe_size.std()
df.side
df.side.str[0]
df.side.str[0].str.upper()
df.side.apply(lambda side: side[0].upper())
df.shoe_size.quantile
df.shoe_size.quantile(0.25)
df.shoe_size < df.shoe_size.quantile(0.25)
df[df.shoe_size < df.shoe_size.quantile(0.25)]
df[df.shoe_size > df.shoe_size.quantile(0.75)]
get_ipython().system('git status')

# -----------------------------------------------------------
# Reading & Writing Data
#   Save the students data to a csv file.
#   Read the data from the csv file back into pandas. What do you notice?
#   Create a data frame based on the profiles.json file. Explore this data frame's structure
#   Write the code necessary to create a data frame based on the results of a SQL query to the numbers database.

import pandas as pd
import numpy as np
import csv

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']
student_number = list(range(1, len(students) + 1))
shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
side_of_classroom = np.random.choice(['left', 'right'], len(students))
favorite_number = np.random.randint(1, 11, len(students))
pd.DataFrame(dict(name=students,
    student_no=student_number,
    shoe_size=shoe_sizes,
    side=side_of_classroom,
    favorite_number=favorite_number))
df = pd.DataFrame(dict(name=students,
    student_no=student_number,
    shoe_size=shoe_sizes,
    side=side_of_classroom,
    favorite_number=favorite_number))
df
students = pd.DataFrame(dict(name=students,
    student_no=student_number,
    shoe_size=shoe_sizes,
    side=side_of_classroom,
    favorite_number=favorite_number))
print('print dictionary')    
print(students)
#  --------------- dump it out to csv
students.to_csv(r'students.csv',index=False)
#  --------------- read it back from csv to dataframe
print('\n')
print('print dictionary loaded from csv')        
csv_df = pd.read_csv('students.csv')
print(csv_df)

# -------------------------
import pymysql as py
import pandas as pd
from pydataset import data
from sqlalchemy import create_engine
from env import user, host, pw

#   function to read env.py and establish connection to sql database
def get_connection(db, user, host, password):
#    url = f'mysql+mysqlconnection://{user}:{password}:@host/{db}
    url = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, db)
    dbc = create_engine(url)
    return dbc

conn = get_connection('numbers', user, host, pw)
print(' user:', user, ' host:', host, 'pw:', pw)

#  Regression is Module 5,   find my group in module 5, and return list of all students in that group
numbers_groupsdf = pd.read_sql('SELECT * FROM numbers_with_more_groups', conn)
print(numbers_groupsdf)