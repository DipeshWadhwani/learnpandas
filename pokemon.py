import pandas as pd

df = pd.read_csv("pokemon.csv")
# print(df)  # this will add first 5 and last five in the terminal when you will run.

# to show everything in the terminal .to_string() is used

print(df.to_string()) # this will show every row every column not the truncated version
