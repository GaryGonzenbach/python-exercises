# get_ipython().run_line_magic('matplotlib', 'qt')   #   use for jupyter notebooks only
import matplotlib.pyplot as plt
import pymysql as py
import pandas as pd
from pydataset import data
from sqlalchemy import create_engine
from datetime import datetime
from env import user, host, pw

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
# -----------------------------------------------------------------------
#   Problem 1
#  Use pandas to convert the following list to a numeric series:
#  ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
prices = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
prices = pd.Series(prices).str.replace('$','').str.replace(',','')
prices.astype('float') 

# another method would be to loop through the series and format each
#   row individually.  works exactly the same way
prices = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
prices_series = pd.Series(prices)
for x in prices_series:
    ystring = x
    ystring = x.replace('$','').replace(',','')
    prices_series[x] = ystring
# --------------------------------------------------------------------------
# Problem 2,  Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
#   How many rows and columns are there?
#   What are the data types?
df = data('mpg')
data('mpg', show_doc=True)
print(' There are x rows, y columns:')
print(df.shape)         # 234 rows  and 11 columns
print('\n')
print(' The dtypes:')
print(df.dtypes)
print(df.info())
# print('\n')
# print(df)    
#  ------------------
# do any cars that have better city mileage than highway mileage?
# creates an index, the value can be either True or False,  (len then returns the total count)
#  so, this line is not effective at evaluating the condition
len( (df.cty > df.hwy) )  
# # this method returns a single bool,  either True of False
#  so this will tell you if this condition is met at least once 
#  in the dataset,  or False if none of the records meet this condition
(df.cty > df.hwy).any()
# using brackets like this, indexes the condition onto 
#   cty and hwy, and returns a dataframe only where that condition is True
#   so if you wanted to count the number of times this condition is tru
#    in a dataset,  this would be one way to do it
len( df[ (df['cty'] > df['hwy'])]  )
# there are zero cars that have better cty than highway mileage
# ---------------------
# Create a column named mileage_difference this column should contain 
#   the difference between highway and city mileage for each car.
df['mileage_diff'] = df.hwy - df.cty
df['mileage_diff']
#----------------------
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
# ----------------------
model_df = df.groupby('model').agg({'hwy': 'mean', 'cty': 'mean'})
model_df
print(' The number of different car models is ',len(model_df))
# --------------------
trans_df = df.groupby('trans').agg({'hwy': 'mean', 'cty': 'mean'})
trans_df
print(' Automatic trans has better mileage')
#  other method using a lambda to simplify down to only two transmission types
#    create a new column that simplifies the tran column into only 'auto' or 'manual
find_t_type = lambda trans: 'auto' if trans[0:4] == 'auto' else 'manual'
df.trans.apply(find_t_type)
#  todo; cant get the lambda to work,  it runs but doesn't seem to affect the dataframe....    need to get help with this
#----------------------------------------------------------------------
# Problem 3, Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
#   How many rows and columns are there?
#   What are the data types?
#   What is the the weight of the fastest animal?
#   What is the overal percentage of specials?
#   How many animals are hoppers that are above the median speed? 
#     What percentage is this?

df = data('Mammals')
# data('Mammals', show_doc=True)
# print(df.shape)         # 234 rows  and 11 columns
# print(df.head())
#  -   looks like this isn't working,    need to follow up why
#  df.sort_values(by='speed', ascending=False)
#  - find the fastest,   all three of these different methods work
df.speed.max()
df.nlargest(5, 'speed')
max_speed_index = df.speed.idxmax()
df.loc[max_speed_index]
#   What is the overal percentage of specials?
num_specials = len(df.loc[df['specials'] == True])
percent_specials = (num_specials / len(df)) * 100
#   How many animals are hoppers that are above the median speed? 
#     What percentage is this?
median_speed_all = df.speed.median()
(len(df.loc[ (df['hoppers'] == True) & (df['speed'] > median_speed_all) ]) / 107) * 100
#----------------------------------------------------------------------
# Problem 4,
#  Getting data from SQL databases
#   Create a function named get_db_url. It should accept a username, hostname, password, 
#      and database name and return a url formatted like in the examples in this lesson.
#    Use your function to obtain a connection to the employees database.
#       Read the employees and titles tables into two separate data frames
#  ------------------------
# Visualize the number of employees with each title.
#    Visualize how frequently employees change titles.
#     Use the .join method to join the employees and titles data frames together
#      For each title, find the hire date of the employee that was hired most recently with that title.
conn = get_connection('employees', user, host, pw, driver='pymysql')           
employees_df = pd.read_sql('SELECT * FROM employees;', conn)
titles_df = pd.read_sql('SELECT * FROM titles;', conn)
#  better to load the entire titles dataframe rather than let SQL do it in the WHERE claus, (faster)  - then you also have enough
#    information in the dataframe to figure out how many different titles each employee had
#  first, see how many different employees per title
#    use the value_counts method to give the number of counts for each unique value of title
#     value_counts requires specifying a single column or a series (title)      
#       look at current titles only 
current_titles = titles_df[titles_df.to_date > datetime.now().date()]
current_titles
current_titles.title.value_counts().plot.bar()
#  Use the .join method to join the employees and titles data frames together
#    For each title, find the hire date of the employee that was hired most recently 
#      with that title (maximum hire date).
#      have to add suffix to left dataframe because one of the column names is not unique
#       pandas join defaults to left,   so need to specific inner join
employees_with_titles = employees_df.join(titles_df, on='emp_no', lsuffix='_emp', how='inner')
employees_with_titles.groupby('title')[['hire_date']].max()
# ----------------------------------------------------------------------------
# Problem 5,  Explore the data from the chipotle database. 
#    Write a python script that will use this data to answer the following questions:
#     What is the total price for each order?
#      What are the most popular 3 items?
#       Which item has produced the most revenue?
connection = get_connection('chipotle', user, host, pw, driver='pymysql')  
orders = pd.read_sql('SELECT * FROM orders', connection)
orders.item_price.str.replace('$', '').astype('float')
orders.item_price = orders.item_price.str.replace('$', '').astype('float')
# orders.head(20)
orders.groupby('order_id').sum()
orders[['order_id', 'item_price']].groupby('order_id').sum()
orders.head(10)
#     What is the total price for each order?
grouped_orders = orders[['order_id', 'item_price']].groupby('order_id').sum()
#     What are the most popular 3 items?
orders.item_name.value_counts().head(7)
#       Which item has produced the most revenue?,   group sum on price
orders[['item_name', 'item_price']].groupby('item_name').sum().nlargest(7, 'item_price')
