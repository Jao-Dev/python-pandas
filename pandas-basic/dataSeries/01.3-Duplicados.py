"""
Write a Pandas program to create a Series from a dictionary
with duplicate values and then remove duplicates.
"""

import pandas as pd;

ds = set(pd.Series([1,1,2,2,3,3,4,5,6,"a","a","B"]));

print(ds);