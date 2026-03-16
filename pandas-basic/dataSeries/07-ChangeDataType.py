import pandas as pd;

pdSerie = pd.Series([100, 200, "python", 300.12, 400]);
print("Data Series original:");
print(pdSerie);

pdSeriesFloat = pd.to_numeric(pdSerie, errors="coerce");
print("Data Series convertido:");
print(pdSeriesFloat);
 