import pandas as pd

#To check for the system max rows
# print(pd.options.display.max_rows)

#How to read a .csv file
df = pd.read_csv("customer.csv")
# df = pd.read_csv("customer.csv", index_col="First Name")

# print(df)
# print(df.to_string())  #Use this if you want to print all the file

#SELECTION BY COLUMN
#print(df["Customer Id"]) #It becomes a series because of how it is presented
#print(df["Website"])
# print(df[["First Name", "Phone 1", "Email"]].to_string())

#SELECTION BY ROWS
# print(df.loc["Debra":"Fred", ["Country", "City"]])
#Integer based selector
# print(df.iloc[0:11:2, 0:2])

#EXERCISE
# customers = input("Enter Customer's name: ")

# try:
#     print(df.loc[customers])
# except KeyError:
#     print(f"{customers} not found")


#Filtering means keeping rows that match a condition
# index_num = df[df["Index"] >= 95]
#nc orrect print(index_num.to_string())
# first_char = df[df["Index"] == 76]
# print(first_char)

#Agregate Functions reduces a set of values into a single summary value 
#used to summarize and analyze data oftem used with groupby()
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

#SINGLE COLUMN
# print(df["Index"].mean())
# print(df["Index"].sum())
# print(df["Index"].min())
# print(df["Index"].max())
# print(df["Index"].count())

#GROUPBY()
# group = df.groupby("First Name")
# print(group["Index"].mean())
# print(group["Index"].sum())
# print(group["Index"].min())
# print(group["Index"].max())
# print(group["Index"].count())

#DATA CLEANING 
#The process of fixing/removing incomplete, incorrect or irrelevant data
#1. Drop irrelevant columns
df = df.drop(columns=["Website", "Subscription Date", "Email", "Customer Id"])
print(df)

#2. How to handle missing data
# df = df.dropna(subset=["First Name"])
# print(df.to_string())
# df = df.fillna({"First Name" : "None"})

#3. Fix inconsistent values
# df["First Name"] = df["First Name"].replace({"Sheryl": "Henry"})

#4. Standardize Text
df["Last Name"] = df["Last Name"].str.lower()

#5. Fix data type
# df["Index"] = df["Index"].astype(int)

#6. Removind duplicate values
df = df.drop_duplicates()
print(df.to_string())

#How to read a .json file
# df = pd.read_json("data.json")

# print(df.to_string())