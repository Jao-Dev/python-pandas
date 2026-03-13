import pandas as pd;
import numpy as np;

rng = np.random.default_rng(seed=100);
rngN = rng.integers(1, 14, 40);
s1 = pd.Series(rngN);

print("Série original:")
print(s1)

frequencia = s1.value_counts().sort_index()

print("\nFrequência de cada valor único:")
print(frequencia)