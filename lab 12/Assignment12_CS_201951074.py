'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 12
from scipy import stats
import pandas as pd


read_data = pd.read_csv('cookie_cats.csv')
print(read_data.head())

# ##############################
# ######### question 1 #########
# ##############################

# Perform t-test on given data and make conclusion from derived p-value.

ans = stats.ttest_ind(read_data[read_data.version == 'gate_30'].sum_gamerounds,read_data[read_data.version == 'gate_40'].sum_gamerounds, equal_var=False)
print(f't-value : {ans.statistic:.4f}')
print(f'p-value for single sided test: {ans.pvalue / 2:.4f}')