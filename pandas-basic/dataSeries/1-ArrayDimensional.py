"""
Write a Pandas program to create a Series from a list
containing different data types and then filter out
elements of a specific type.

"""

import pandas as pd;
ds = pd.Series([2, 4, 6, 8, 10, "a", "b", "Olá Mundo", "Teste"]);

filtro = ds[ds.apply(lambda x: isinstance(x,str))]

for i in filtro:
    print(i)
