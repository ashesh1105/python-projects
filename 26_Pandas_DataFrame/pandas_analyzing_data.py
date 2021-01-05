import pandas as pd

# Below helps view complete dataframe in pandas, hence, it helps print it too
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_csv('data.csv')

# Print first 10 rows of the dataframe. Note: 10 includes the header row too
# With our .csv file, header column takes 1st row, so we get 9 data rows
print(df.head(10))

# If head does not specify number of rows, it returns first 5 rows
print(df.head())

# Last 5 rows of the dataframe
print(df.tail())

# Last 12 rows
print(df.tail(12))

# Info
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

# This is how we get occurrence %age of one or more column data combinations
print('%age of occurrences of Duration and Pulse value combinations:')
print(df[['Duration', 'Pulse']].value_counts(normalize=True).head(20))

