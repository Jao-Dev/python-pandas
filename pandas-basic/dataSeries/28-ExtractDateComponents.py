import pandas as pd;

s1 = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20']);
s1a = pd.to_datetime(s1, unit='ns');

diaMes = s1a.dt.day
diaAno = s1a.dt.dayofyear
numSemana = s1a.dt.isocalendar().week
diaSemana = s1a.dt.day_name()

print("Original Series:\n\n", s1a, "\n\n");
print("Dia do mês:\n", diaMes.tolist());
print("Dia do ano:\n", diaAno.tolist());
print("Número da semana:\n", numSemana.tolist());
print("Dia da semana:\n", diaSemana.tolist());