import pandas as pd;
import numpy as np;

d1 = pd.DataFrame({
    "col1":[1,4,3,4,5],
    "col2":[4,5,6,7,8],
    "col3":[7,8,9,0,1]
});

print("Original:\n",d1)
print(
    "\nSem a 'col3':\n",
    d1.loc[:, d1.columns != "col3"]
)