import pandas as pd;
import numpy as np;

d1 = pd.DataFrame({
    "col1":[1,4,3,4,5],
    "col2":[4,5,6,7,8],
    "col3":[7,8,9,0,1]
});

filtro = d1.drop([2,4]);

print("Original:\n",d1);
print("\n\nApós deletar a 2ª e 4ª colunas:\n",filtro);