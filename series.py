import pandas as pd


# Series - Series is a 1D array its like 1 column in a table or excel sheet. It can hold any data type like int, float, string etc.

mygarage = ["Mercedes","Bmw","Rolls Royce","Lamborghini","Ferrari"]
mygarage_series = pd.Series(mygarage)
print(mygarage_series)

# we can do arithmatic operations too

cal = {
    "Day1" : 1935,
    "Day2" : 2005,
    "Day3" : 2369,
    "Day4" : 1999
}

cal_series = pd.Series(cal)  # this will show all the days and calaries

# There is loc and iloc, loc is location and iloc is index location in loc is we write ["Day1"] it will show value for Day1 and if we do ["Day2"] it will show values of Day2, iloc is the same but instead of ["Day1"] etc we write index numbers which starts from 0.

print(cal_series.loc["Day1"]) # this will show the calaries of day 1
print(cal_series.iloc[1]) # this will also show the calaries of day 2

# if you want to add, subtract, multiply, or divide the values in the series you can do that too like this 

cal_series.loc["Day3"] += 500  # it will add 500 cal in day3 

print(cal_series.loc["Day3"])
print(cal_series)
