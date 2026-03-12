import pandas as pd;

pdSeries = pd.Series(["100", "200", "python", "300.12", "400"]);

print("Series original:\n",pdSeries);

novosItens = pd.Series(["500", "php"])

pdSeries = pd.concat([pdSeries, novosItens], ignore_index=True)
print("Series com mais alguns dados:\n", pdSeries)