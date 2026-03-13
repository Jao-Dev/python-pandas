import pandas as pd;
import numpy as np;

ns = np.random.RandomState(100)
s1 = pd.Series(ns.normal(10, 4, 20));
resultado = np.percentile(s1, q=[0, 25, 50, 75, 100]);

print("Original Series:\n",s1);
print("Mínimo, 25%, média, 75%, máximo:");
print(resultado);

