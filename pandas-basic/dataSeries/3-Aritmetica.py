import pandas as pd;

s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])

soma = s1+s2;
subtracao = s1-s2;
multiplicacao = s1*s2;
divisao = s1/s2;

print(f"Soma: {soma.values}");
print(f"Subtração: {subtracao.values}");
print(f"Multiplicação: {multiplicacao.values}");
print(f"Divisão: {divisao.values}");

