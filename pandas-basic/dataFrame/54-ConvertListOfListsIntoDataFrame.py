import pandas as pd
my_lists = [['col1', 'col2'], [2, 4], [1, 3]]

colunas = my_lists.pop(0)
d1 = pd.DataFrame(my_lists, columns=colunas)


print(d1)