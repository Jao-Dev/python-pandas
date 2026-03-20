import pandas as pd;
import numpy as np;

d1 = pd.DataFrame({
    "col1":[1,4,3,4,5],
    "col2":[4,5,6,8,7],
    "col3":[7,8,9,0,1]
});


print("Linha que a col1 tem o valor máximo:\n",d1["col1"].idxmax());
print("Linha que a col2 tem o valor máximo:\n",d1["col2"].idxmax());
print("Linha que a col3 tem o valor máximo:\n",d1["col3"].idxmax());