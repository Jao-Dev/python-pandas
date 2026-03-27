import pandas as pd

d1 = pd.DataFrame({
    'X': [1, 6, 8, 3, 7],
    'Y': [5, 2, 9, 4, 1],
    'Z': ['one', 'one', 'two', 'two', 'one']
})

d2 = d1.set_index(["Z", "X"])

print(d2.loc["two"])