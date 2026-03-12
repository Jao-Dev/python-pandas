import pandas as pd;

pdList = pd.Series([
    ["Red", "Green", "White"],
    ["Red", "Black"],
    ["Yellow"]
]);

print("Series list original:");
print(pdList);
print(pdList.dtype);
print();

pdSeries = pdList.explode().reset_index(drop=True);
print("Uma Series:");
print(pdSeries);
print(pdSeries.dtype);



