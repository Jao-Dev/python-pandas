import pandas as pd;
import numpy as np;

d1 = pd.DataFrame({
    "col1":[1,4,3,4,5],
    "col2":[4,5,6,7,8],
    "col3":[7,8,9,0,1]
});

if "col4" not in d1.columns:
    print("Col4 não está presente no DataFrame");
else:
    print("Col4 está presente no DataFrame");
if "col1" not in d1.columns:
    print("Col1 não está presente no DataFrame");
else:
    print("Col1 está presente no DataFrame");