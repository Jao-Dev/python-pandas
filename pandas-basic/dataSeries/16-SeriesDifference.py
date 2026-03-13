import pandas as pd;

s1 = pd.Series([1,2,3,4,5]);
s2 = pd.Series([2,4,6,8,10]);
s3 = s1[~s1.isin(s2)];

print("s1:\n",s1);
print("s2:\n",s2);

print("Itens presentes na s1 que não estão na s2:\n",s3);