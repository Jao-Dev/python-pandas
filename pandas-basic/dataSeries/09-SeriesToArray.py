import pandas as pd;

pdSeries = pd.Series([100, 200, "python", 300.12, 400]);
print("Data Series original:")
print(pdSeries);
print();

pdArray = pd.Series.__array__(pdSeries);
print("De Series para array:")
print(pdArray)
print(type(pdArray))
