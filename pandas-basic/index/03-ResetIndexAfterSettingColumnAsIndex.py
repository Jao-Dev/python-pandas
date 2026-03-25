import pandas as pd

d1 = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']});

d2 = d1.set_index("t_id");
d3 = d2.reset_index(drop=True);

print("Original:\n",d1);
print("\nColuna como index:\n",d2);
print("\nReset do index:\n",d3);