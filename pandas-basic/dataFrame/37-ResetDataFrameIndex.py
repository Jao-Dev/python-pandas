import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    };
d1 = pd.DataFrame(exam_data);

filtro = d1.drop([2,4]);
d2 = filtro.reset_index(drop=True)



print("Original:\n",d1);
print("\n\nApós deletar a 2ª e 4ª colunas:\n",filtro);
print("\n\nApós resetar o index:\n",d2);