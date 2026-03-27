import pandas as pd

d1 = pd.DataFrame({
    'A': [1, 6, 8, 3, 7],
    'B': [5, 2, 9, 4, 1]
})

filtro = d1[d1["A"]>4]
print(filtro)