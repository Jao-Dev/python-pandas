import pandas as pd;
import numpy as np;

d1 = pd.DataFrame({
    "col1":[1,4,3,4,5],
    "col2":[4,5,6,7,8],
    "col3":[7,8,9,0,1]
});
nr = pd.DataFrame({"col1":[10], "col2":[11], "col3":[12]})
d2 = pd.concat([d1, nr], ignore_index=True)

print(d2)