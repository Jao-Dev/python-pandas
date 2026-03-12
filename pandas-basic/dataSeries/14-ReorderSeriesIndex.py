import pandas as pd;

letras=["A","B","C","D","E"];
numeros=[1,2,3,4,5];
ogSeries = pd.Series(numeros, index=letras);

print(ogSeries)

reordenado = ogSeries.reindex(["B","A","C","D","E"])
print(reordenado)