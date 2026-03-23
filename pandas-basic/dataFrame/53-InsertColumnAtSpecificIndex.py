import pandas as pd;
import numpy as np;

d1 = pd.DataFrame({
    "col2":[4,5,6,7,8],
    "col3":[7,8,9,0,1]
});

d2 = [1,4,3,4,5];

print("Original:\n",d1);

d1.insert(0, "col1", d2)
print("\n\nApós adicionar a coluna:\n", d1);
