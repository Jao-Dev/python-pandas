import pandas as pd;
from dateutil.parser import parse;

s1 = pd.Series(["Jan 2015", "Feb 2016", "Mar 2017", "Apr 2018", "May 2019"]);
s1a = pd.to_datetime(s1, unit="ns");
s1b = s1a.map(lambda d: parse(f"{d.year}-{d.month:02d}-11"))
print(s1b)