import pandas as pd;
from collections import Counter;

s1 = pd.Series(["Red", "Green", "Orange", "Pink", "Yellow", "White"]);

filtrado = s1.map(lambda x: sum([Counter(x.lower()).get(i,0) for i in list("aeiou")])>=2);

print(s1[filtrado])