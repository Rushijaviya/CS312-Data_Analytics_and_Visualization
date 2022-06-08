'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 4
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_egg = pd.read_csv("Egg_Production_2007_2012.csv")
print(data_egg.head())
data_milk = pd.read_csv("Milk_Production_2007_2012.csv")
print(data_milk.head())

# ##############################
# ######### question 1 #########
# ##############################

# Merge two data into a data frame such that the new data frame has multi-level columns (like
# years under milk/eggs). Try to change the column names if required.

data_merge = pd.merge(data_egg,data_milk,on ='States/Uts')
data_merge.head()
newColumns = [("","States/Uts"), ("Eggs","2007-08"),  ("Eggs","2008-09"),  ("Eggs","2009-10"),  ("Eggs","2010-11"),  ("Eggs","2011-12"),  ("Milk","2007-08"), ("Milk","2008-09"), ("Milk","2009-10"), ("Milk","2010-11"), ("Milk","2011-12")]
data_merge.columns = pd.MultiIndex.from_tuples(newColumns)
data_merge.head()

# ##############################
# ######### question 2 #########
# ##############################

# Present the production of milk in Gujarat, Kerala, Andhra Pradesh, Uttar Pradesh and Panjab
# on 2007-2008 as a Pie chart. The pie chart should consist of proportion in percentage and labels
# for each piece.

data_states = ["Gujarat", "Kerala", "Andhra Pradesh", "Uttar Pradesh", "Punjab"]
data = data_milk[data_milk["States/Uts"].isin(data_states)]["2007-08"]
data_color = sns.color_palette('pastel')[0:5]
label=data_states
explode=[0.02,0.02,0.02,0.04,0.05]
plt.pie(data, labels=label,colors = data_color,autopct = '%0.0f%%',explode = explode,shadow = 'True',textprops = {'color': 'Green','fontsize':14},wedgeprops = {'linewidth': 3},rotatelabels = 'true')
plt.show()

# ##############################
# ######### question 3 #########
# ##############################

# Plot five pie charts of egg production in Gujarat, Kerala, Andhra Pradesh, Uttar Pradesh and
# Panjab given five years range. Each pie chart should represent the egg production in above five
# states for a given year.

data_states = ["Gujarat", "Kerala", "Andhra Pradesh", "Uttar Pradesh", "Punjab"]

data1_egg = data_egg[data_egg["States/Uts"].isin(data_states)]["2007-08 (In lakh nos.)"]
data2_egg = data_egg[data_egg["States/Uts"].isin(data_states)]["2008-09 (In lakh nos.)"]
data3_egg = data_egg[data_egg["States/Uts"].isin(data_states)]["2009-10 (In lakh nos.)"]
data4_egg = data_egg[data_egg["States/Uts"].isin(data_states)]["2010-11 (In lakh nos.)"]
data5_egg = data_egg[data_egg["States/Uts"].isin(data_states)]["2011-12 (In lakh nos.)"]
data_color = sns.color_palette('pastel')[0:5]
explode=[0,0.07,0,0,0.08]
fig, axs = plt.subplots(2, 3, figsize=(15, 15))

axs[0, 0].pie(data1_egg, labels=data_states,colors = data_color, autopct="%.1f%%",explode = explode,shadow = 'True',textprops = {'color': 'Red','fontsize':12},wedgeprops = {'linewidth': 3},rotatelabels = 'true')
axs[0, 0].set_title("2007-08")
axs[0, 1].pie(data2_egg, labels=data_states,colors = data_color, autopct="%.1f%%",explode = explode,shadow = 'True',textprops = {'color': 'Blue','fontsize':12},wedgeprops = {'linewidth': 3},rotatelabels = 'true')
axs[0, 1].set_title("2008-09")
axs[0, 2].pie(data3_egg, labels=data_states,colors = data_color, autopct="%.1f%%",explode = explode,shadow = 'True',textprops = {'color': 'Black','fontsize':12},wedgeprops = {'linewidth': 3},rotatelabels = 'true')
axs[0, 2].set_title("2009-10")
axs[1, 0].pie(data4_egg, labels=data_states,colors = data_color, autopct="%.1f%%",explode = explode,shadow = 'True',textprops = {'color': 'Purple','fontsize':12},wedgeprops = {'linewidth': 3},rotatelabels = 'true')
axs[1, 0].set_title("2010-11")
axs[1, 1].pie(data5_egg, labels=data_states,colors = data_color, autopct="%.1f%%",explode = explode,shadow = 'True',textprops = {'color': 'Green','fontsize':12},wedgeprops = {'linewidth': 3},rotatelabels = 'true')
axs[1, 1].set_title("2011-12")
axs[1, 2].axis('off')

# ##############################
# ######### question 4 #########
# ##############################

# Plot Staked Area Chart that represents state wise (i.e. states are in x axis) production of eggs
# (y-axis). There would be five stacked colors and each color represents the production of egg in
# a state. The egg production for each state should be normalized over the year range.

data = data_egg[data_egg["States/Uts"].isin(data_states)]
data.index = data["States/Uts"]
data.drop(columns=["States/Uts"], inplace=True)
data.columns = ["2007-08", "2008-09", "2009-10", "2010-11", "2011-12"]

plt.stackplot(data.index, data["2007-08"], data["2008-09"], data["2009-10"], data["2010-11"], data["2011-12"], labels=data.columns)
plt.legend(loc=(1.0, 0.6))
plt.show()

norm = data.div(data.sum(axis=1), axis=0)
norm1 = data.div(data.mean(axis=1), axis=0)

plt.stackplot(norm.index, norm["2007-08"], norm["2008-09"], norm["2009-10"], norm["2010-11"], norm["2011-12"], labels=norm.columns)
plt.legend(loc=(1.0, 0.6))

plt.show()