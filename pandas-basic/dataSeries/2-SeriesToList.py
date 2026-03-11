import pandas as pd;

df = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

dfList = df.to_list();
print(f"Lista: {dfList}");
print(f"Tipo: {type(dfList)}");
