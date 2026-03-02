import pandas as pd

df = pd.read_csv("pokemon.csv",index_col="Name") # this will read the csv file and set the index column as "Name" which is the name of the pokemon
# print(df)  # this will add first 5 and last five in the terminal when you will run.

print(df.to_string())# to show everything in the terminal .to_string() is used

 # this will show every row every column not the truncated version

#df_json = pd.read_json("pokemon.json") # this will read the json file and set the index column as "Name" which is the name of the pokemon
#print(df_json.to_string())

# SELECTION by column
print(df["Weight"].to_string())
print(df["Height"].to_string())

# for multuple columns

print(df[["Height","Weight"]].to_string())

#SELECTION by row
print(df.loc["Bulbasaur"]) # this will show the first row of the dataframe
print(df.iloc[0:11]) # this will show the first 10 rows of the dataframe but it will not include the 11th row because in python the index starts from 0 and it goes up to n-1 where n is the number of rows in the dataframe. so if we want to include the 11th row we have to write iloc[0:12] because it will include the 11th row as well.
print(df.loc["Bulbasaur":"Charmander"]) # this will show the rows from Bulbasaur to Charmander including both of them because in loc we can use the labels of the index to select the rows. so it will include both the start and end labels.

print(df.loc["Bulbasaur":"Charmander",["Height","Weight"]]) # this will show the rows from Bulbasaur to Charmander including both of them and only the columns Height and Weight because in loc we can use the labels of the index to select the rows and we can also use the labels of the columns to select the columns. so it will include both the start and end labels for rows and it will include only the specified columns.

pokemon = input("Enter the name of Pokemon you want to know about: ")
try:
    print(df.loc[pokemon])
except KeyError:
    print("Pokemon not found in the database.")



