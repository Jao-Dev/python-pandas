import pandas as pd;

s1=pd.Series([2, 4, 6, 8, 10]);
s2=pd.Series([1, 3, 5, 7, 10]);

print("Série 1:")
print(s1);
print("Série 2:")
print(s2)

print("Valores iguais:")
print(s1==s2);

print("Maior que:")
print(s1>s2);

print("Menor que:")
print(s1<s2);