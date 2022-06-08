'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 3
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from joypy import joyplot 


# ##############################
# ######### question 1 #########
# ##############################

# Present the data from dataset using three appropriate plots explained in Class.

data=pd.read_csv("grains_production_india_from_2001_to_2017.csv")
print(data)

#data of all grains
grains = data.pivot_table(index="Year")
print(grains)

ax = sns.pointplot(data=grains, dodge=True, join=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)

ax=sns.stripplot(data=grains)
ax=sns.violinplot(data=grains,color="0.4")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)

joyplot(grains,overlap = 0)
plt.show()

# now taking only the data of FOOD GRAINS (CEREALS)
#removing the unwanted columns (all except cereals)
Cereals = data.drop(data.iloc[:,9:], inplace=False, axis=1)
print(Cereals)

ax = sns.pointplot(data=Cereals, dodge=True, join=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)

ax = sns.stripplot(data=Cereals)
ax = sns.violinplot(data=Cereals,color="0.4")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)

joyplot(Cereals,overlap = 0)
plt.show()