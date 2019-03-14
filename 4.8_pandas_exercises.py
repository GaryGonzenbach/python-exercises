import pymysql as py
import pandas as pd
from pydataset import data
from sqlalchemy import create_engine
from env import user, host, pw
# ------------------------------------------------------
# Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
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
    grouped_df['average_mileage'] = (grouped_df['hwy'] + grouped_df['cty']) / 2

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

#---------------------------------------------------------------
# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
#    How many rows and columns are there?
#   What are the data types?
#   What is the the weight of the fastest animal?
#   What is the overal percentage of specials?
#   How many animals are hoppers that are above the median speed? What percentage is this?