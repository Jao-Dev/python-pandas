import pandas as pd

d1 = pd.DataFrame({
    'X': [1, 6, 8, 3, 7],
    'Y': [5, 2, 9, 4, 1],
    'Z': ['one', 'one', 'two', 'two', 'one']
})

print(d1.loc[3])