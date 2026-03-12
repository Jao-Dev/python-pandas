import pandas as pd;

pdSeries = pd.Series([0,1,2,3,4,5,6,7,8,9,10]);

print("Original:\n",pdSeries,"\n");

valor = 6
subset = pdSeries[pdSeries<6];
print("Subset:\n",subset);