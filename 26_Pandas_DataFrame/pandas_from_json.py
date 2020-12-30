import pandas as pd

# Below helps view complete dataframe in pandas, hence, it helps print it too
pd.set_option("display.max_rows", None, "display.max_columns", None)

"""
Json data is noting but a dictionary in Python. It can be read into Pandas Dataframe by pd.read_json method.
"""

df = pd.read_json('data.json')
# If you do not see more than first 5 and last 5 rows while printing it, use df.to_string()
print(df)
"""
Prints df rows and columns with index (since we did not specify it):
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
....
"""

