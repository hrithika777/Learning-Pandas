#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# TASK #1. DEFINE A PANDAS SERIES


# In[6]:


# Pandas is a data manipulation and analysis tool that is built on Numpy.
# Pandas uses a data structure known as DataFrame (think of it as Microsoft excel in Python). 
# DataFrames empower programmers to store and manipulate data in a tabular fashion (rows and columns).
# Series Vs. DataFrame? Series is considered a single column of a DataFrame.

import pandas as pd


# In[1]:


# Let's define a Python list that contains 5 crypto currencies 
crypto_list = ['BTC', 'XRP', 'LTC', 'ADA', 'ETH']


# In[2]:


# Let's confirm the Datatype
type(crypto_list)


# In[7]:


# Let's create a one dimensional Pandas "series" 
# Let's use Pandas Constructor Method to create a series from a Python list
# Note that series is formed of data and associated index (numeric index has been automatically generated) 
# Check Pandas Documentation for More information: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series
# Object datatype is used for text data (String)
crypto_series = pd.Series(data = crypto_list)
crypto_series


# In[8]:


# Let's confirm the Pandas Series Datatype
type(crypto_series)


# In[10]:


# Let's define another Pandas Series that contains numeric values (crypto prices) instead of text data
# Note that we have int64 datatype which means it's integer stored in 64 bits in memory
crypto_prices_series = pd.Series(data = [2000, 500, 2000, 20, 50])
crypto_prices_series


# **MINI CHALLENGE #1:**
# - **Define a Pandas Series named "my_series" that contains your top 3 favourite stocks. Confirm the datatype of "my_series"**

# In[12]:


mylist = ['Facebook', 'Apple', 'Nvidia']

my_series = pd.Series(data = mylist)
my_series


# # TASK #2. DEFINE A PANDAS SERIES WITH CUSTOM INDEX

# In[13]:


# Let's define a Python list that contains 5 Crypto currencies
crypto_list = ['BTC', 'XRP', 'LTC', 'ADA', 'ETH' ]
crypto_list


# In[14]:


# Let's define a python list as shown below. This python list will be used for the Series index:
crypto_labels = ['crypto#1', 'crypto#2', 'crypto#3', 'crypto#4', 'crypto#5']
crypto_labels


# In[15]:


# Let's create a one dimensional Pandas "series" 
# Let's use Pandas Constructor Method to create a series from a Python list
# Note that this series is formed of data and associated labels 
crypto_series = pd.Series(data = crypto_list, index = crypto_labels)


# In[10]:


# Let's view the series


# In[16]:


# Let's obtain the datatype
type(crypto_series)


# **MINI CHALLENGE #2:**
# - **Define a Pandas Series named "my_series" that contains your top 3 favourite stocks. Instead of using default numeric indexes (similar to mini challenge #1), use the following indexes "stock #1", "stock #2", and "stock #3"**

# In[21]:


mylist = ['Apple', 'Nvidia', 'Titan']
myindex = ['stock#1', 'stock#2', 'stock#3']
myseries = pd.Series(data = mylist, index = myindex)
myseries


# # TASK #3. DEFINE A PANDAS SERIES FROM A DICTIONARY

# In[23]:


# A Dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its corresponding value.
# Keys are unique within a dictionary while values may not be. 
# List elements are accessed by their position in the list, via indexing while Dictionary elements are accessed via keys
# Define a dictionary named "my_dict" using key-value pairs
my_dict = {'Employee ID': 1,
          'Employee Name': 'Steve',
          'Salary [$]': 2000,
          'Years with Company': 10}


# In[24]:


# Show the dictionary
my_dict


# In[25]:


# Confirm the dictionary datatype 
type(my_dict)


# In[26]:


# Let's define a Pandas Series Using the dictionary
employee_series = pd.Series(my_dict)
employee_series


# **MINI CHALLENGE #3:**
# - **Create a Pandas Series from a dictionary with 3 of your favourite stocks and their corresponding prices** 

# In[29]:


stock_dict = {'Apple': 10000,
             'Nvidia': 2000,
             'Titan': 40000}
my_stocks = pd.Series(stock_dict)
my_stocks


# # TASK #4. PANDAS ATTRIBUTES

# In[30]:


# Attributes/Properties: do not use parantheses "()" and are used to get Pandas Series Properties. Ex: my_series.values, my_series.shape
# Methods: use parantheses "()" and might include arguments and they actually alter/change the Pandas Series. Ex: my_series.tail(), my_series.head(), my_series.drop_duplicates()
# Indexers: use square brackets "[]" and are used to access specific elements in a Pandas Series or DataFrame. Ex: my_series.loc[], my_series.iloc[]

# Let's redefine a Pandas Series containing our favourite 5 cryptos 
crypto_list = ['BTC', 'XRP', 'LTC', 'ADA', 'ETH']
crypto_series = pd.Series(data = crypto_list)
crypto_series


# In[31]:


# ".Values" attribute is used to return Series as ndarray depending on its dtype
# Check this for more information: https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html#pandas.Series.values
crypto_series.values


# In[32]:


# index is used to return the index (axis labels) of the Series
crypto_series.index


# In[33]:


# dtype is used to return the datatype of the Series ('O' stands for 'object' datatype)
crypto_series.dtype


# In[20]:


# Check if all elements are unique or not


# In[34]:


# Check the shape of the Series
# note that a Series is one dimensional
crypto_series.shape


# **MINI CHALLENGE #4:** 
# - **What is the size of the Pandas Series? (External Research for the proper attribute is Required)**

# In[35]:


crypto_series.size


# # TASK #5. PANDAS METHODS

# In[36]:


# Methods have parentheses and they actually alter/change the Pandas Series
# Methods: use parantheses "()" and might include arguments. Ex: my_series.tail(), my_series.head(), my_series.drop_duplicates()

# Let's define another Pandas Series that contains numeric values (crypto prices) instead of text data
# Note that we have int64 datatype which means it contains integer values stored in 64 bits in memory
crypto_prices = pd.Series(data = [400, 500, 1500, 20, 70])
crypto_prices


# In[23]:


# Let's obtain the sum of all elements in the Pandas Series
crypto_prices.sum()


# In[37]:


# Let's obtain the multiplication of all elements in the Pandas Series
crypto_prices.product()


# In[39]:


# Let's obtain the average
crypto_prices.mean()


# In[38]:


# Let's show the first couple of elements in the Pandas Series
crypto_prices.head(2)


# In[41]:


# Note that head creates a new dataframe 
new_crypto_prices = crypto_prices.head(3)
new_crypto_prices


# **MINI CHALLENGE #5:** 
# - **Show the last 2 rows in the Pandas Series (External Research is Required)** 
# - **How many bytes does this Pandas Series consume in memory? (External Research is Required)**

# In[42]:


crypto_prices.memory_usage()


# In[43]:


crypto_prices.tail(2)


# # TASK #6. IMPORT CSV DATA (1-D) USING PANDAS

# In[44]:


# Pandas read_csv is used to read a csv file and store data in a DataFrame by default (DataFrames will be covered shortly!)
# Use Squeeze to convert it into a Pandas Series (One-dimensional)
# Notice that no foramtting exists when a Series is plotted
BTC_price_series = pd.read_csv('crypto.csv', squeeze = True)


# In[45]:


BTC_price_series


# **MINI CHALLENGE #6:**
# - **Set Squeeze = False and rerun the cell, what do you notice? Use Type to compare both outputs**

# In[46]:


BTC_price_series = pd.read_csv('crypto.csv', squeeze = False)
BTC_price_series


# In[47]:


type(BTC_price_series)


# # TASK #7. PANDAS BUILT-IN FUNCTIONS

# In[48]:


# Pandas works great with pre-existing python functions 
# You don't have to play with pandas methods and directly leverage Python functions
# Check Python built-in functions here: https://docs.python.org/3/library/functions.html
BTC_price_series = pd.read_csv('crypto.csv', squeeze = True)
BTC_price_series


# In[49]:


# Obtain the Data Type of the Pandas Series
type(BTC_price_series)


# In[50]:


# Obtain the length of the Pandas Series
len(BTC_price_series)


# In[51]:


# Obtain the maximum value of the Pandas Series
max(BTC_price_series)


# In[52]:


# Obtain the minimum value of the Pandas Series
min(BTC_price_series)


# **MINI CHALLENGE #7:**
# - **Given the following Pandas Series, convert all positive values to negative using python built-in functions**
# - **Obtain only unique values (ie: Remove duplicates) using python built-in functions**
# - my_series = pd.Series(data = [-10, 100, -30, 50, 100])
# 

# In[53]:


my_series = pd.Series(data = [-10, 100, -30, 50, 100])
my_series


# In[54]:


abs(my_series)


# In[55]:


set(my_series)


# # TASK #8. SORTING PANDAS SERIES

# In[67]:


# Let's import CSV data as follows:
BTC_price_series = pd.read_csv('crypto.csv', squeeze = True)
BTC_price_series


# In[68]:


# You can sort the values in the dataframe as follows
BTC_price_series.sort_values()


# In[69]:


# Let's view Pandas Series again after sorting, Note that nothing changed in memory! you have to make sure that inplace is set to True
BTC_price_series


# In[70]:


# Set inplace = True to ensure that change has taken place in memory 
BTC_price_series.sort_values(inplace = True)


# In[71]:


# Note that now the change (ordering) took place 
BTC_price_series


# In[72]:


# Notice that the indexes are now changed 
# You can also sort by index (revert back to the original Pandas Series) as follows: 
BTC_price_series.sort_index(inplace = True)
BTC_price_series


# **MINI CHALLENGE #8:**
# - **Sort the BTC_price_series values in a decending order instead. Make sure to update values in-memory.**

# In[73]:


BTC_price_series.sort_values(ascending = False, inplace = True)
BTC_price_series


# # TASK #9. PERFORM MATH OPERATIONS ON PANDAS SERIES

# In[74]:


# Let's import CSV data as follows:
BTC_price_series = pd.read_csv('crypto.csv', squeeze = True)
BTC_price_series


# In[75]:


# Apply Sum Method on Pandas Series
BTC_price_series.sum()


# In[76]:


# Apply count Method on Pandas Series
BTC_price_series.count()


# In[77]:


# Obtain the maximum value
BTC_price_series.max()


# In[79]:


# Obtain the minimum value
BTC_price_series.min()


# In[80]:


# My favourite: Describe! 
# Describe is used to obtain all statistical information in one place 
BTC_price_series.describe()


# **MINI CHALLENGE #9:**
# - **Obtain the average price of the BTC_price_series using two different methods**

# In[81]:


BTC_price_series.mean()


# In[83]:


BTC_price_series.sum()/BTC_price_series.count()


# # TASK #10. CHECK IF A GIVEN ELEMENT EXISTS IN A PANDAS SERIES

# In[86]:


# Let's import CSV data as follows:
BTC_price_series = pd.read_csv('crypto.csv', squeeze = True)
BTC_price_series


# In[87]:


# Check if a given number exists in a Pandas Series values
# Returns a boolean "True" or "False"
17887 in BTC_price_series.values


# In[90]:


# Check if a given number exists in a Pandas Series index
550 in BTC_price_series.index


# In[93]:


# Note that by default 'in' will search in Pandas index and not values
550 in BTC_price_series


# **MINI CHALLENGE #10:**
# - **Check if the stock price 399 exists in the BTC_price_series Pandas Series or not**
# - **Round stock prices to the nearest integer and check again**

# In[94]:


399 in BTC_price_series.values


# In[95]:


price_series = round(BTC_price_series)
price_series


# # EXCELLENT JOB!

# In[96]:


399 in price_series


# # MINI CHALLENGE SOLUTIONS

# **MINI CHALLENGE #1 SOLUTION:**
# - **Define a Pandas Series named "my_series" that contains your top 3 favourite stocks. Confirm the datatype of "my_series"**

# In[51]:


# Let's define a Python list that contains 3 top stocks
my_list = ['Facebook','Apple','Nvidia'] 
my_series = pd.Series(data = my_list) 
my_series


# In[52]:


type(my_series)


# **MINI CHALLENGE #2 SOLUTION:**
# - **Define a Pandas Series named "my_series" that contains your top 3 favourite stocks. Instead of using default numeric indexes (similar to mini challenge #1), use the following indexes "stock #1", "stock #2", and "stock #3"**

# In[53]:


# Let's define a Python list that contains 3 stocks as follows
my_list = ['Facebook','Apple','Nvidia'] 

# Let's define a python list as shown below. This python list will be used for the Series index:
my_labels = ['stock #1', 'stock #2', 'stock #3']


# In[54]:


# Let's create a one dimensional Pandas "series" 
# Let's use Pandas Constructor Method to create a series from a Python list
# Note that this series is formed of data and associated labels 
my_series = pd.Series(data = my_list, index = my_labels)
my_series


# **MINI CHALLENGE #3 SOLUTION:**
# - **Create a Pandas Series from a dictionary with 3 of your favourite stocks and their corresponding prices** 
# 

# In[55]:


stocks = {'Facebook': 3000, 
          'Apple'   : 400,
          'Nvidia'  : 2200}
print(stocks)


# In[56]:


# Let's define a Pandas Series Using the dictionary
my_series = pd.Series(stocks)
my_series


# **MINI CHALLENGE #4 SOLUTION:** 
# - **What is the size of the Pandas Series? (External Research is Required)**

# In[57]:


# size is used to return the size of the series
crypto_series.size


# **MINI CHALLENGE #5 SOLUTION:** 
# - **Show the last 2 rows in the Pandas Series (External Research is Required)** 
# - **How many bytes does this Pandas Series consume in memory? (External Research is Required)**

# In[58]:


crypto_prices.tail(2)


# In[59]:


crypto_prices.memory_usage()


# In[ ]:





# **MINI CHALLENGE #6 SOLUTION:**
# - **Set Squeeze = False and rerun the cell, what do you notice? Use Type to compare both outputs**

# In[60]:


BTC_price_series = pd.read_csv('crypto.csv', squeeze = False)
# Note that when you set Squeeze = False, the data is stored in a DataFrame by default. 
# DataFrame is simply used to store multi dimensional data as compares to Pandas Series that only holds 1-D dataset 
# Note that DataFrames has proper formatting when you attempt to view them as shown below 
# Note that Pandas Series has no formatting


# In[61]:


BTC_price_series


# In[62]:


type(BTC_price_series)


# In[63]:


BTC_price_series = pd.read_csv('crypto.csv', squeeze = True)
type(BTC_price_series)


# **MINI CHALLENGE #7 SOLUTION:**
# - **Given the following Pandas Series, convert all positive values to negative using python built-in functions**
# - **Obtain only unique values (ie: Remove duplicates) using python built-in functions**
# - my_series = pd.Series(data = [-10, 100, -30, 50, 100])
# 

# In[64]:


my_series = pd.Series(data = [-10, 100, -30, 50, 100])
my_series


# In[65]:


abs(my_series)


# In[66]:


set(my_series)


# **MINI CHALLENGE #8 SOLUTION:**
# - **Sort the BTC_price_series values in a decending order instead. Make sure to update values in-memory.**

# In[67]:


BTC_price_series.sort_values(ascending = False, inplace = True) 
BTC_price_series


# **MINI CHALLENGE #9 SOLUTION:**
# - **Obtain the average price using two different methods**

# In[68]:


# Obtain the average - Solution #1
BTC_price_series.sum()/BTC_price_series.count()


# In[69]:


# Obtain the average - Solution #s
BTC_price_series.mean()


# In[ ]:





# **MINI CHALLENGE #10 SOLUTION:**
# - **Check if the stock price 399 exists in the BTC_price_series Pandas Series or not**
# - **Round stock prices to the nearest integer and check again**

# In[70]:


399 in BTC_price_series.values


# In[71]:


prices_series = round(BTC_price_series)
prices_series


# In[72]:


399 in prices_series.values


# In[ ]:





# In[ ]:




