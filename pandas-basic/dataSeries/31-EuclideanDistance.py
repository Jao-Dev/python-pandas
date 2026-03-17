import pandas as pd;
import numpy as np;

rng = np.random.default_rng(seed=100);
s1 = pd.Series(rng.integers(1,15,10));
s2 = pd.Series(rng.integers(1,15,10));

d = np.linalg.norm(s1-s2);


print("Original Series: \n",s1,s2);
print("\n\nDistância Euclidiana entre as series: ", d);