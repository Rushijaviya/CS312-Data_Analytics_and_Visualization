'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 14

from matplotlib import pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns

read_data=pd.read_csv("IPL_Auction_2022_FullList.csv")
print(read_data.head())

# ##############################
# ######### question 1 #########
# ##############################

# Create contingency table from ”Specialism” and ”Batting” type of player.

table1=pd.crosstab(read_data["Specialism"],read_data["Batting"],margins=True)
print(table1)

table2=pd.crosstab(read_data["Specialism"],read_data["Batting"],margins=False)
print(table2)


# Perform Chi square test on data in contingency table.

df=3
data_chi = stats.chi2.rvs(table2)
sns.histplot(data_chi,kde=True)
plt.show()

chisq, pvalue, df, expected = stats.chi2_contingency(table2)
print(f'Observed chi2: {chisq:.4f}')
print(f'p-value: {pvalue:.4f}')