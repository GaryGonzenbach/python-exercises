import numpy as np
print(' 4.7 numpy exercises ')

# Exercise 1)
#  How many negative numbers are there
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
less_than_zero = a < 0
n_true = less_than_zero.sum()
print('Exercise 1:  There are ',n_true,' negative numbers in the array.')

# Exercise 2)
#  How many positive numbers are there
greater_than_zero = a > 0
n_true = greater_than_zero.sum()
print('Exercise 2:  There are ',n_true,' positive numbers in the array.')

# Exercise 3)
# How many even positive numbers are there?
greater_than_zero_even = (a>0)%2 == 0
n_true = greater_than_zero_even.sum()
print('Exercise 3:  There are ',n_true,' EVEN positive numbers in the array.')

# Exercise 4 
#  If you were to add 3 to each data point, how many positive numbers would there be?
b = a + 3
greater_than_zero = b > 0
n_true = greater_than_zero.sum()
print('Exercise 4:  Once you add 3 to each value in the array, there are now ',n_true,' positive numbers.')

# Exercise 5
# If you squared each number, what would the new mean and standard deviation be?
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
c = np.square(a)
c_stddev = c.std()
c_mean = c.mean()
print('Exercise 5: If you square the array, the standard dev = ',c_stddev,' and the mean is ',c_mean)

# Exercise 6
# A common statistical operation on a dataset is centering. 
#  This means to adjust the data such that the center of the 
#   data is at 0. This is done by subtracting the mean 
#     from each data point. Center the data set.
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a_stddev = a.std()
a_mean = a.mean()
b = a - a_mean
b_stddev = b.std()
b_mean = b.mean()

print('Exercise 6: Center the array, the old mean = ',a_mean,' and the new mean is ',b_mean)

# Exercise 7)
# Calculate the z-score for each data point. 
#   Recall that the z-score is given by:
#      z =  (data_pnt - mean) / stddev 
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a_stddev = a.std()
a_mean = a.mean()
b = (a - a_mean) /  a_stddev
print('Exercise 7: The z-score array is :  ',b)

#Exercise 8 
# Life w/o numpy to life with numpy
## Setup 1
a8 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
sum_of_a = a8.sum()
min_of_a = a8.min()
max_of_a = a8.max()
mean_of_a = a8.mean()
product_of_a = a8.prod()
squares_of_a = np.square(a8)
odds_in_a  = a8[a8%2==1]  # conditionally selecting a subset of an array
evens_in_a = a8[a8%2==0]  # conditionally selecting a subset of an array

# life in two dimensions, refactoring
import numpy as np
b = [ [3,4,5], [6,7,8] ]
print(' b array ',b)
b_np = np.array(b)
c_npsum = b_np.sum(axis=0)
print('after numpy sum axis = 0: ',c_npsum)
