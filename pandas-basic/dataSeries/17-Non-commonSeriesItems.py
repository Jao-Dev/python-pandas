import pandas as pd;

s1 = pd.Series([1,2,3,4,5]);
s2 = pd.Series([2,4,6,8,10]);

ns2 = s1[~s1.isin(s2)]

ns1 = s2[~s2.isin(s1)]

non_common = pd.concat([ns1, ns2]).sort_values().reset_index(drop=True);

print("Valores não presentes em ambas as séries:")
print(non_common)