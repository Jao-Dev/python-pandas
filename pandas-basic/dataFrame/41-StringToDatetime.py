import pandas as pd
import numpy as np

s1 = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000']);

dt = pd.to_datetime(s1);

print("Original:\n", s1);
print("\nConvertido:\n",dt);