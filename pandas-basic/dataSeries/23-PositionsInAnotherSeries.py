import pandas as pd;
import numpy as np;

s1 = pd.Series([1,2,3,4,5,6,7,8,9,10]);
s2 = pd.Series([1,3,5,7,10]);

posicoes = s1[s1.isin(s2)].index

print("Posições dos elementos em s1 que estão em s2:")
print(posicoes)