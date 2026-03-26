import pandas as pd;
import numpy as np;


d1 = pd.date_range(start="2025-03-26 07:15:00", freq="ME", periods=10);
d2 = pd.DataFrame({"col1":[100, 110, 117, 150, 112, 99, 129, 135, 140, 150]},
                  index=d1);
print(d2)