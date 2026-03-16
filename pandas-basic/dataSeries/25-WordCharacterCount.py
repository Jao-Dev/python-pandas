import pandas as pd;

s1 = pd.Series(["php", "python", "java", "c#"]);

words = s1.str.len();

print(words)