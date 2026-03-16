import pandas as pd;

s1 = pd.Series(["php", "python", "java", "c#"]);

s1a = s1.str[0].str.upper()+s1.str[1:-1]+s1.str[-1].str.upper()

print(s1a)