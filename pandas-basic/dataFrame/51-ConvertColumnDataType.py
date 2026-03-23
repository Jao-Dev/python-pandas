import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9.1, 16.5, 12.77, 9.21, 20.22, 14.5, 11.34, 8.8, 19.13],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    };
d1 = pd.DataFrame(exam_data);

print("Original:\n",d1);
print(d1.dtypes);
print("\n\nDataType modificado em 'score':\n",d1.astype({"score":"int64"}).dtypes);
