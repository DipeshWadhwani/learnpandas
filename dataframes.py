import pandas as pd


# DataFrame - DataFrame is the 2D array it contains rows and columns like it is in excel 

family = {
    "Name" : ["Dipesh","Kushal","Harsha","Devanand","Bhavesh","Kishan","Lata","Naresh"],
    "Age" : [18,13,42,52,30,34,49,55]
}

df = pd.DataFrame(family)
print(df)
