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

conn = get_connection('ada_students', user, host, pw)
print(' user:', user, ' host:', host, 'pw:', pw)

#  Regression is Module 5,   find my group in module 5, and return list of all students in that group
studentdf = pd.read_sql('SELECT * FROM student_groups WHERE student_id = 673 AND module_id = 5;', conn)
print(studentdf)

#  my group 4
groupdf = pd.read_sql('SELECT * FROM student_groups WHERE group_id = 4 AND module_id = 5;', conn)
print(groupdf)

#  students in group 4

student_groupdf = pd.read_sql('SELECT * FROM students WHERE student_id = 673 OR student_id = 664 OR student_id = 670;', conn)
print(student_groupdf)