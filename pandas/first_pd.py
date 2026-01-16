import pandas as pd

#Series: It is pandas 1-Dimensional labeled array that can hold any data type.
#Think of it like a single column in a spreadsheet (1-Dimensional)

# data = [100, 102, 104, 200, 202]
# series = pd.Series(data, index=["a", "b", "c", "d", "e"])
# print(series[series < 200])
# #.loc and .iloc is used to slice out values


calories = {
    "Day 1" : 1750,
    "Day 2" : 2000,
    "Day 3" : 1950,
    "Day 4" : 1700,
    "Day 5" : 2100,
    "Day 6" : 1850,
    "Day 7" : 1900
}
series = pd.Series(calories)
# series.loc["Day 7"] += 300
print(series[series >= 2000])


#DataFrame: A tabular data structure with rows and columns. (2-Dimensional)
#Similar to Excel spreadsheet
data = {
    "Name" : ["Ayo", "Jesse", "Rasheed", "Alameen"],
    "Status" : ["Single", "Married", "Married", "Married"]
}
df = pd.DataFrame(data, index=["Kali", "Ubuntu", "Mint", "Ubuntu"])
# print(df)

#Add a new column
df["Job"] = ["All-round Expert", "Cybersecurty Expert", "Software Developer", "Software Engineer"]
# print(df)

#Add a new row
new_row = pd.DataFrame([{"Name" : "Israel", "Status" : "Married", "Job" : "Web3 Developer"}], index=["Windows"])
df = pd.concat([df, new_row])
print(df)

