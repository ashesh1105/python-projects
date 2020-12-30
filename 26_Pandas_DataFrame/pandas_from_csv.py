import pandas as pd

# Below helps view complete dataframe in pandas, hence, it helps print it too
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Read CSV file as Pandas DataFrame
df = pd.read_csv('data.csv')
# Note: if you see only first 5 and last 5 rows, use df.to_string() while printing it.
print(df)
"""
# Prints tabular structure with columns as: Duration, Pulse, Maxpulse, Calories and index on the left column:
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
...
"""







if __name__ == '__main__':
    pass