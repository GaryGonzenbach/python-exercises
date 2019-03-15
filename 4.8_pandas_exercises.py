import pymysql as py
import pandas as pd
from pydataset import data
from sqlalchemy import create_engine
from env import user, host, pw
#   Problem 1
#  Use pandas to convert the following list to a numeric series:
#  ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
prices = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
prices = pd.Series(prices).str.replace('$','').str.replace(',','')
prices.astype('float') 
# ------------------------------------------------------
# Problem 2,  Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
#   How many rows and columns are there?
#   What are the data types?
df = data('mpg')
# data('mpg', show_doc=True)
print(' There are x rows, y columns:')
print(df.shape)         # 234 rows  and 11 columns
print('\n')
print(' The dtypes:')
print(df.dtypes)
# print('\n')
# print(df)    
#  ---------------------------------------------------------------
# do any cars that have better city mileage than highway mileage
# 
# creates an index, the value can be either 
#     True or False,  (len then returns the total count)
#  so, this line is not effective at evaluating the condition
len( (df.cty > df.hwy) )  
# 
# this method returns a single bool,  either True of False
#  so this will tell you if this condition is met at least once 
#  in the dataset,  or False if none of the records meet this condition
(df.cty > df.hwy).any()
# 
# using brackets like this, indexes the condition onto 
#   cty and hwy, and returns a dataframe only where that condition is True
#   so if you wanted to count the number of times this condition is tru
#    in a dataset,  this would be one way to do it
len( df[ (df['cty'] > df['hwy'])]  )
# there are zero cars that have better cty than highway mileage
# 
# ------------------------------------------------------------
# Create a column named mileage_difference this column should contain 
#   the difference between highway and city mileage for each car.
#
df['mileage_diff'] = df.hwy - df.cty
#  display it
df['mileage_diff']

#---------------------------------------------------------------
# on average, which manufacturer has the best miles per gallon
# df.describe()    #  just to show the keys
# df.groupby( ['manufacturer'] ).groups.keys()   ,  #  just to show the keys
#  aggregate the dataframe to manufacturer and calculate the average hwy and cty first
grouped_df = df.groupby('manufacturer').agg({'hwy': 'mean', 'cty': 'mean'})
# now loop and average the "hwy" "cty" averages, then sort in Desc order
for i in grouped_df:
    grouped_df['average_mileage'] = (grouped_df['hwy'] * 0.45 + grouped_df['cty'] * 0.55)

grouped_df.sort_values(by='average_mileage', ascending=False, inplace=True)
grouped_df
print(' The number of different car manufacturers is ',len(grouped_df))
# -----------------------------------------------------------
model_df = df.groupby('model').agg({'hwy': 'mean', 'cty': 'mean'})
model_df
print(' The number of different car models is ',len(model_df))
# --------------------
trans_df = df.groupby('trans').agg({'hwy': 'mean', 'cty': 'mean'})
trans_df
print(' Automatic trans has better mileage')

#  other method
#    create a new column that simplifies the tran column into only 'auto' or 'manual
find_t_type = lambda tran: 'auto' if tran[0:4] == 'auto' else 'manual'
df.trans.apply(find_t_type)


#---------------------------------------------------------------
# Problem 3, Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
#    How many rows and columns are there?
#   What are the data types?
#   What is the the weight of the fastest animal?
#   What is the overal percentage of Prspecials?
#   How many animals are hoppers that are above the median speed? 
#     What percentage is this?





#---------------------------------------------------------------
# Problem 4,
#  Getting data from SQL databases
#   Create a function named get_db_url. It should accept a username, hostname, password, 
#      and database name and return a url formatted like in the examples in this lesson.
#    Use your function to obtain a connection to the employees database.
#       Read the employees and titles tables into two separate data frames

import pymysql as py        #   python sql driver
import pandas as pd
from pydataset import data
from sqlalchemy import create_engine
from env import user, host, pw
import matplotlib.pyplot as plt
%matplotlib qt   

# this function just returns the url string to pass to get_connection
def get_db_url(db, user, host, password):
    #    url = f'mysql+mysqlconnection://{user}:{password}:@host/{db}
    url = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, db)
    return(url)

#   function to read env.py and establish connection to sql database
def get_connection(db, user, host, password, driver='pymsql'):
#    url = f'mysql+mysqlconnection://{user}:{password}:@host/{db}
    url = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, db)
    dbc = create_engine(url)
    return dbc
#  ------------------------------------------
# Visualize the number of employees with each title.
#    Visualize how frequently employees change titles.
#     Use the .join method to join the employees and titles data frames together
#      For each title, find the hire date of the employee that was hired most recently with that title.

conn = get_connection('employees', user, host, pw, driver='pymysql')           
employees_df = pd.read_sql('SELECT * FROM employees;', conn)
titles_df = pd.read_sql('SELECT * FROM titles WHERE to_date > NOW();', conn)
title_groupdf = titles_df.groupby('title').agg({'emp_no': 'count'})
titles_df.title.value_counts().plot.bar

#  probably better to load the entire titles dataframe rather than let SQL do it in the WHERE claus, (faster)  - then you also have enough
#    information in the dataframe to figure out how many different titles each employee had

#   how many titles does each employee have  (on entire titles dataframe)
titles.emp_no.value_counts()  
plt.subplots_adjust(left=0.15)

#   join the data using pandas
#  have to add suffix to left dataframe because one of the column names is not unique
#    pandas join defaults to left,   so need to specific inner join
employees.join(titles, on='emp_no', lsuffix='_emp', how='inner')

#  find hire date of most recent employee

employees_with_titles.groupby('title'),[['hire_date']]

