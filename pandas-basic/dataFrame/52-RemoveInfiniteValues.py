import pandas as pd
import numpy as np
from numpy import inf;
df = pd.DataFrame([1000, 2000, 3000, -4000, np.inf, -np.inf])

print("Original:\n",df);
print("\n\nAlterado:\n",df.replace([np.inf, -np.inf], np.nan));