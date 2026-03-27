import pandas as pd

d1 = pd.DataFrame({
    'X': [1, 6, 8, 3, 7],
    'Y': [5, 2, 9, 4, 1],
    'Z': [3, 8, 6, 2, 9]
})

d2 = d1[["X","Y"]]
print(
    d2
)