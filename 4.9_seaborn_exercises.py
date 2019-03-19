# 4.9_seaborn_exercises 
import pymysql as py        #   python sql driver
import pandas as pd
from pydataset import data
from sqlalchemy import create_engine
from env import user, host, pw
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib qt   

# Exercises
# Create a file named 4.9_seaborn_exercises.py for this exercise.
# Use the iris database to answer the following quesitons:
# What does the distribution of petal lengths look like?
# Is there a correlation between petal length and petal width?
# Would it be reasonable to predict species based on sepal width and sepal length?
# Which features would be best used to predict species?

'''    temp turn off the first example
iris = sns.load_dataset('iris')
get_ipython().run_line_magic('matplotlib', 'qt')
# sns.set_style('whitegrid')
sns.distplot(iris.petal_length)
plt.title('Iris Histogram - Petal Length')
plt.show()
sns.relplot(data=iris, x = 'petal_length', y = 'petal_width', hue = 'species')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Iris Petal Length and Width')
plt.show()
sns.pairplot(data=iris, hue = 'species')
plt.show()
'''
# Exercise 1
# Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. 
#  Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. 
#  What do you notice?
#  Plot the x and y values from the anscombe data. Each dataset should be in a separate column.
anscombe = sns.load_dataset('anscombe')
anscombe.describe()
get_ipython().run_line_magic('matplotlib', 'qt')
# groups_df = anscombe.groupby('dataset')
# print(groups_df)
# groups_df.describe()
# get_ipython().run_line_magic('matplotlib', 'qt')

# for x in groups_df:
#    dataset = groups_df.dataset
    

