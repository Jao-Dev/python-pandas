import pandas as pd;
import numpy as np;

d1 = pd.DataFrame({
    "col1":[1,4,3,4,5],
    "col2":[4,5,6,7,8],
    "col3":[7,8,9,0,1]
});

d2 = pd.DataFrame();

print("DataFrame original:\n",d2);
print("Após adcionar:\n",pd.concat([d2,d1]));