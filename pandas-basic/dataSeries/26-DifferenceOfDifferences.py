import pandas as pd;
import numpy as np;

rng = np.random.default_rng(seed=100);
s1 = pd.Series(rng.integers(1, 15, 7));

print(s1.diff().tolist())
print(s1.diff().diff().tolist())