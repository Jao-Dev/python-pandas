import pandas as pd
import numpy as np

s1 = pd.Series(['100', '200', 'python', '300.12', '400']);
s2 = pd.Series(['10', '20', 'php', '30.12', '40']);

"""d1 = pd.DataFrame({
    "0":s1,
    "1":s2
});"""

d2 = pd.concat([s1, s2], axis=1);


print("Data Series:\n",s1,s2);
print("\n\nNovo DataFrame com séries combinadas:\n",d2);