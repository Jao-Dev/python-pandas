import pandas as pd;
import numpy as np;

s1 = pd.Series(np.random.randint(0, 50, [22]));
filtro = s1.iloc[[0,2,6,11,21]];

print("Original Series:\n",s1,"\n");
print("Items extraídos dada as posições:\n",filtro);