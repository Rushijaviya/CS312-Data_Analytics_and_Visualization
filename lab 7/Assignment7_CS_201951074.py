'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 7

import pandas as pd
import seaborn as sns
import math
import matplotlib.pyplot as plt
import numpy as np

# ##############################
# ######### question 1 #########
# ##############################

# Compute the correlation coefficients of columns of the ”All India CPI” data. 
# Plot the correlation as heat map.

cpi_data=pd.read_csv("All_India_CPI.csv")   # all india cpi
# print(cpi_data)
print(cpi_data.corr())
sns.heatmap(cpi_data.corr())

# ##############################
# ######### question 2 #########
# ##############################

# Compute the Contingency table between ”toss winner” and ”Winner” columns of the data ”IPL
# Matches 2008-2020” data.

ipl_data=pd.read_csv("IPL Matches 2008-2020.csv")   # ipl matches
# print(ipl_data)
crosstab_data = pd.crosstab(ipl_data['toss_winner'], ipl_data['winner'], margins = False)
print(crosstab_data)

# ##############################
# ######### question 3 #########
# ##############################

# Plot the hexagonal binning of ”Price” and ”Landsize” columns of Melborn housing price data.

melb_data=pd.read_csv("melb_data.csv")  # melb_data
# print(melb_data)

fig=plt.hexbin(melb_data["Landsize"], melb_data["Price"], gridsize = 100,cmap ='Greens') 
plt.xlabel("Landsize")
plt.ylabel("Price")
plt.xlim(0,4000)
plt.ylim(0,1500000)
fig2 = plt.colorbar(fig) 