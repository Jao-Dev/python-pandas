import pandas as pd;

s1 = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20']);

s1a = pd.to_datetime(s1, unit='ns');

print(s1a)