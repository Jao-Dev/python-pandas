import pandas as pd;
import numpy as np;

d1 = pd.DataFrame({
    "col1":(1,2,3),
    "col2":(4,5,6),
    "col3":(7,8,9)
});

d2 = d1.rename(columns={"col1":"Column1", "col2":"Column2", "col3":"Column3"});

print("Original:\n",d1);
print("\nRenomeado:\n",d2);