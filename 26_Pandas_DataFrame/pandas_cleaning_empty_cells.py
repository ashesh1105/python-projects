import pandas as pd

# Below helps view complete dataframe in pandas, hence, it helps print it too
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_csv('data.csv')

print(df.info())
"""
Prints a lot of useful info about our data, like number of columns, rows, column names, non-null data in each column, etc
 <class 'pandas.core.frame.DataFrame'>
  RangeIndex: 169 entries, 0 to 168
  Data columns (total 4 columns):
   #   Column    Non-Null Count  Dtype  
  ---  ------    --------------  -----  
   0   Duration  169 non-null    int64  
   1   Pulse     169 non-null    int64  
   2   Maxpulse  169 non-null    int64  
   3   Calories  164 non-null    float64
  dtypes: float64(1), int64(3)
  memory usage: 5.4 KB
  None
"""

# Let's remove the rows with empty cells
new_df = df.dropna()    # dropna() returns a new dataframe, will not change the original one
print(new_df.info())
"""
Now prints below. Note: 5 rows got removed since there were empty cells for Calories column on those rows!
<class 'pandas.core.frame.DataFrame'>
Int64Index: 164 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  164 non-null    int64  
 1   Pulse     164 non-null    int64  
 2   Maxpulse  164 non-null    int64  
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 6.4 KB
None
"""

"""
Replace Empty Values
by fillna() method. Unlike dropna(), you do not have to remove entire row and just replace empty cells with specified data
"""
df.fillna(130, inplace=True)
print(df.info())
"""
See, now it shows that all the rows are full. You can print entire df to check that too with 130 on earlier empty cells:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  169 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None
"""

"""
You can also fillna() with mean, median or mode of a column
x = x = df["Calories"].mean()   # average value in a column
x = df["Calories"].median()     # sort the column and the value that comes in the middle (50 %ile)
x = df["Calories"].mode()[0]    # most frequently occurring value in a column
df["Calories"].fillna(x, inplace = True)
"""

# Cleaning Date column, say we have NaT or date like a number, we can do following on pd
# Our csv or json does not has date column, so below line needs to remain commented out
# df['Date'] = pd.to_datetime(df['Date'])

# We can also replace a cell and change the data there, like below for index 60, Duration column 210 -> 45
print(f"Duration column on index 60 before: {df.loc[60, 'Duration']}")
df.loc[60, 'Duration'] = 45
print(f"Duration column on index 60 after: {df.loc[60, 'Duration']}")

# There are still Duration more than 120 on some cells, like 170 on index 79, 180 on index 90, etc.
# Let's change any Duration data which is more than 120 to 120
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120

print(df.loc[90, 'Duration'])   # prints 120

# Below will remove rows where Duration is more than 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

# Find out rows that are duplicates. It prints a boolean with indices. True meaning row at that index is duplicate
# Below output shows rows at indices 36, 37, 38, 40, 71, 113, 155 are duplicates
print(df.duplicated())


# We can remove the duplicate rows by drop_duplicates method:
print(len(df))  # prints 169
df.drop_duplicates(inplace=True)
print(len(df))  # prints 162, meaning 7 duplicate rows are now gone!



