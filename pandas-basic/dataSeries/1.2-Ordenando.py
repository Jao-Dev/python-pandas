"""
Write a Pandas program to create a Series
with a custom index from a NumPy array
and then reorder the series
based on the index in descending order.
"""

import pandas as pd;
import numpy as np;

arrayNp = np.array(["teste", 1, 3, 25, "array", 4]);
indexPd = pd.Series(arrayNp, index=[1001, 1002, 1003, 1004, 1005, 1006]);

index_ordenado = indexPd.sort_index(ascending=False)

print(index_ordenado)
