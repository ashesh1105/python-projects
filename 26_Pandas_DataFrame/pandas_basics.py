import pandas as pd

# Below helps view complete dataframe in pandas, hence, it helps print it too
pd.set_option("display.max_rows", None, "display.max_columns", None)

# A quick example on Pandas Dataframe
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(type(myvar))  # Prints <class 'pandas.core.frame.DataFrame'>
print(myvar)    # Prints dataframe as below. Note: Index (0, 1, 2) comes out as a bonus!
"""
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
"""

# Pandas version
print(pd.__version__)   # Prints the version. In my case, 1.1.5

"""
Series
A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.
Labels
If noting else is specified, the values are labeled with their index number. First value has index 0, second value has
index 1 etc. This label can be used to access a specified value.
"""
a = [1,7,2]
myvar = pd.Series(a)
print(myvar)
"""
prints:
0    1
1    7
2    2
dtype: int64
"""
print(myvar[1]) # prints 7

# Create own labels in a Series
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
"""
prints:
x    1
y    7
z    2
dtype: int64
"""
# Now, we can access an item by its label
print(myvar['x'])   # prints 1

# Key/Value object as Series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
"""
prints:
day1    420
day2    380
day3    390
dtype: int64
"""

# What if we supply index for first few elements? It'll create Series with just those labels and items underneath them!
myvar = pd.Series(calories, index=["day1", "day2"])
print(f'\n{myvar}')
"""
prints:
day1    420
day2    380
dtype: int64
"""

"""
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
Series is like a column, a DataFrame is the whole table.
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
"""

# Create a DataFrame from two Series:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)
"""
Prints:
   calories  duration
0       420        50
1       380        40
2       390        45
"""

# Locate Row(s) - the loc attribute of pandas. It returns Pandas Series
print(df.loc[0])
"""
prints:
calories    420
duration     50
Name: 0, dtype: int64
"""

# Locate Row 0 and 1
print(df.loc[[0, 1]])   # Note: for multiple indices, we need to give it as [[idx1, idx2, idx3..]]
"""
prints row 0 and 1:
   calories  duration
0       420        50
1       380        40
"""

# Named Indexes. With index argument you can name your own indexes
df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df)
"""
prints:
      calories  duration
day1       420        50
day2       380        40
day3       390        45
"""

# Locate named indexes
print(df.loc['day2'])
"""
prints:
calories    380
duration     40
Name: day2, dtype: int64
"""











if __name__ == '__main__':
    pass

