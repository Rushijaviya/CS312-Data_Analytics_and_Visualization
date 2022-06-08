'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 1
import pandas as pd
import json
import sys

# ##############################
# ######### question 1 #########
# ##############################

# question 1 part 1
# read the csv file and save it in dataframe

data1=pd.read_csv("district_level_service_msme.csv")
print(data1)

# question 1 part 2
# read the json file and save it in dataframe

f=open("district_level_manufacturing_msme.json")
df=json.load(f)
# print(df)

column=pd.DataFrame(df['fields'])['label'].tolist()
#print(column)

data2=pd.DataFrame(df['data'],columns=column)
print(data2)

# ##############################
# ######### question 2 #########
# ##############################

# find total "Small" Manufacturing MSME in india

# first find the state wise total "Small" Manufacturing MSME
data2["SMALL"]=data2["SMALL"].astype("int") # to use sum() fucntion we convert data type of column "SMALL" to int  
result=data2.groupby("STATE_NAME").sum()["SMALL"]  
# print(result)

# sum the state wise "Small" Manufacturing MSME to get total "Small" Manufacturing MSME in india
print(f"Total Small Manufacturing MSME in India: {result.sum()}")  

data2["SMALL"]=data2["SMALL"].astype("object") # convert back to original data type

# ##############################
# ######### question 3 #########
# ##############################

# state wise total number of "Micro","Small" and "Medium" Services MSE

result2=data1.groupby("STATE_NAME").sum()
print(result2[["MICRO","SMALL","MEDIUM"]])    # using double square brackets we can select multiple columns from DataFrame

result2[["MICRO","SMALL","MEDIUM"]].to_csv("question3.csv") # save into csv file

# ##############################
# ######### question 4 #########
# ##############################

# Join the both the data frame based on common STATE NAME, DISTRICT NAME, Lg Dist Code and Last Updated.

#print(data1.dtypes)
#print(data2.dtypes)

# As we have different data type for column "Lg_Dist_Code" in dataframe we need to convert in same data type to merge
data2["Lg_Dist_Code"] = data2["Lg_Dist_Code"].astype(int)  # change type to "int"

#print(data1.dtypes)
#print(data2.dtypes)

# now we can merge 
result4=pd.merge(data2,data1,left_on=["STATE_NAME","Lg_Dist_Code","DISTRICT_NAME","Last_Updated"], right_on=["STATE_NAME","Lg_Dist_Code","DISTRICT_NAME","Last_Updated"])
print(result4)

# ##############################
# ######### question 5 #########
# ##############################

# Create a Pivot Table having rows STATE NAME and columns Service and Manufacturing "MSME" as show in below. 
# Use "Sum" to add up district wise number.

# print(result4.dtypes)
# we need data type of columns "MICRO_x", "SMALL_x", "MEDIUM_x" to be "int" to use "Sum" function.
result4["MICRO_x"]=result4["MICRO_x"].astype("int")   #conver to int
result4["SMALL_x"]=result4["SMALL_x"].astype("int")   #conver to int
result4["MEDIUM_x"]=result4["MEDIUM_x"].astype("int") #conver to int

# make pivot table
print(result4.pivot_table(["MEDIUM_y","MEDIUM_x","MICRO_x","MICRO_y","SMALL_x","SMALL_y"],index="STATE_NAME",aggfunc='sum'))
