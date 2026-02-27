import pandas as pd


# DataFrame - DataFrame is the 2D array it contains rows and columns like it is in excel 

family = {
    "Name" : ["Dipesh","Kushal","Harsha","Devanand","Bhavesh","Kishan","Lata","Naresh"],
    "Age" : [18,13,42,52,30,34,49,55]
}

df = pd.DataFrame(family, index=[1,2,3,4,5,6,7,8])
print(df)

# add column 
df["Job"] = ["Student","Student","Housewife","Businessman","Job","Job","Housewife","Businessman"]
print(df)

# add row

new_members = pd.DataFrame([{"Name": "Sneha","Age": 29,"Job" : "Housewife"},{"Name" : "Vrishti","Age" : 3,"Job": "Kid"}], index = [9,10])
df = pd.concat([df,new_members])

print(df)

#this is another way to add row
df.loc[11] = ["Monishka", 17, "Student"] # this will add row with index 11 and the values in the list   
print(df)