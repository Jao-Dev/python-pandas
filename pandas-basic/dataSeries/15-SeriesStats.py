import pandas as pd;

x = pd.Series([1,2,3,4,5,7,3,2,9,1]);

print("Original Data Series:\n", x);
print(x.dtype);
print("Mean:\n",x.mean());
print("Standard deviation:\n",x.std());