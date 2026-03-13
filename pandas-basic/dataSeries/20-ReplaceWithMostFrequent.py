import pandas as pd;
import numpy as np;

s1 = pd.Series(np.random.randint(1, 7, [15]));

top2 = s1.value_counts().head(2).index
s1 = s1.astype(object)

filtro = ~s1.isin(top2)
s1.loc[filtro] = "Other"

print("Top 2 frequências\n", s1.value_counts().loc[top2])
print(s1)
