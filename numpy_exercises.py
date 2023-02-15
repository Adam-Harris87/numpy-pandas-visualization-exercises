#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[134]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[3]:


# 1. How many negative numbers are there?
sum(a < 0)


# In[4]:


# 2. How many positive numbers are there?
sum(a > 0)


# In[5]:


# 3. How many even positive numbers are there?
sum((a > 0) & (a % 2 == 0))


# In[6]:


# 4. If you were to add 3 to each data point, how many positive numbers would there be?
sum(a + 1 > 0)


# In[7]:


# 5. If you squared each number, what would the new mean and standard deviation be?
np.mean(a ** 2), np.std(a ** 2)


# In[136]:


#  6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.
centered = a - a.mean()
centered


# In[9]:


# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# Z = (x-μ) / σ
z_scores = (a - a.mean()) / a.std()
z_scores


# ## 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# In[10]:


# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:


# In[11]:


# Exercise 1 - Make a variable called sum_of_a to hold the 
# sum of all the numbers in above list
sum_of_a = 0
for num in a:
    sum_of_a += num
sum_of_a


# In[12]:


# Exercise 2 - Make a variable named min_of_a to hold the 
# minimum of all the numbers in the above list
min_of_a = min(a)
min_of_a


# In[13]:


# Exercise 3 - Make a variable named max_of_a to hold the 
# max number of all the numbers in the above list
max_of_a = max(a)
max_of_a


# In[14]:


# Exercise 4 - Make a variable named mean_of_a to hold the 
# average of all the numbers in the above list
mean_of_a = sum_of_a / len(a)
mean_of_a


# In[15]:


# Exercise 5 - Make a variable named product_of_a to hold the 
# product of multiplying all the numbers in the above list together
product_of_a = 1
for num in a:
    product_of_a = product_of_a * num
product_of_a


# In[16]:


# Exercise 6 - Make a variable named squares_of_a. It should hold 
# each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [x ** 2 for x in a]
squares_of_a


# In[17]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [x for x in a if x % 2 == 1]
odds_in_a


# In[18]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [x for x in a if x % 2 == 0]
evens_in_a


# #### What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...

# In[19]:


## Setup 2: Consider what it would take to find the 
# sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[132]:


# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

b_array = np.array(b)
b_array.sum()


# In[36]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
b_array.min()


# In[37]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
b_array.max()


# In[38]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
b_array.mean()


# In[131]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
b_array.prod()


# In[42]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
b_array ** 2


# In[45]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
b_array[b_array % 2 == 1]


# In[46]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
b_array[b_array % 2 == 0]


# In[48]:


# Exercise 9 - print out the shape of the array b.
b_array.shape


# In[49]:


# Exercise 10 - transpose the array b.
b_array.transpose()


# In[60]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b_array.flatten().tolist()


# In[90]:


# Exercise 12 - reshape the array b to be a list of 6 lists, 
# each containing only 1 number (6 x 1)
b_list = [[num] for num in b_array.flatten().tolist()]
b_list


# In[92]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable 
# is a numpy array prior to using numpy array methods.


# In[93]:


c_array = np.array(c)


# In[95]:


# Exercise 1 - Find the min, max, sum, and product of c.
c_array.min(), c_array.max(), c_array.sum(), c_array.prod()


# In[96]:


# Exercise 2 - Determine the standard deviation of c.
c_array.std()


# In[97]:


# Exercise 3 - Determine the variance of c.
c_array.var()


# In[98]:


# Exercise 4 - Print out the shape of the array c
c_array.shape


# In[99]:


# Exercise 5 - Transpose c and print out transposed result.
c_array.transpose()


# In[100]:


# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c_array, c)


# In[106]:


# Exercise 7 - Write the code necessary to sum up the result 
# of c times c transposed. Answer should be 261
np.sum(c * c_array.transpose())


# In[107]:


# Exercise 8 - Write the code necessary to determine the 
# product of c times c transposed. Answer should be 131681894400.
np.prod(c * c_array.transpose())


# In[108]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


# In[109]:


d_array = np.array(d)


# In[121]:


# Exercise 1 - Find the sine of all the numbers in d
np.sin(d_array)


# In[122]:


# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d_array)


# In[123]:


# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d_array)


# In[124]:


# Exercise 4 - Find all the negative numbers in d
d_array[d_array < 0]


# In[125]:


# Exercise 5 - Find all the positive numbers in d
d_array[d_array > 0]


# In[126]:


# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d_array)


# In[127]:


# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d_array))


# In[128]:


# Exercise 8 - Print out the shape of d.
d_array.shape


# In[129]:


# Exercise 9 - Transpose and then print out the shape of d.
d_array.transpose().shape


# In[130]:


# Exercise 10 - Reshape d into an array of 9 x 2
d_array.reshape((9,2))

