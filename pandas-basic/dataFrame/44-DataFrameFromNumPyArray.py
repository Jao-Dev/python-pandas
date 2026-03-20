import pandas as pd;
import numpy as np;

indexSP = [f"Index{i+1}" for i in range(15)];
valores = np.random.randint(0, 100, (15,3));
d1 = pd.DataFrame(valores, index=indexSP, columns=["Column1","Column2", "Column3"])

print(d1)

