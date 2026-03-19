import pandas as pd;
import numpy as np;

d1 = pd.DataFrame({
    "col1":[1,4,3,4,5],
    "col2":[4,5,6,7,8],
    "col3":[7,8,9,0,1]
});

d1.to_csv("csv27.csv", sep="\t", index=False);

d1csv = pd.read_csv("csv27.csv")
print(d1csv)