import pandas as pd;
import numpy as np;

s1 = pd.Series(np.random.randint(1, 10, [10]));

filtro = s1%5==0
s2 = s1.loc[filtro]

print("Original Series:\n", s1);
print("Múltiplos de 5:\n",s2);