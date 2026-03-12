import pandas as pd;

pdSeries = pd.Series(["100", "200", "python", "300.12", "400"]);
print("Series original:\n", pdSeries, "\n");

ordenado = pdSeries.sort_values();
print(ordenado);