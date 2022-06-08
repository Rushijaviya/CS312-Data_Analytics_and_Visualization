'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 13

import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

read_data = pd.read_csv('cookie_cats.csv')
print(read_data.head())

# ##############################
# ######### question 1 #########
# ##############################

# Perform ANOVA-test on given data and make conclusion from derived p-value.

var_temp=read_data.set_index("version")
df=var_temp.loc["gate_30"].reset_index()
df["gate_40"]=var_temp.loc["gate_40"].reset_index()["sum_gamerounds"]
df["gate_30"]=var_temp.loc["gate_30"].reset_index()["sum_gamerounds"]
df=df.iloc[:,5:]
print(df.head())


# Derivation using Observed means method 
variance_observed = read_data.groupby('version').mean().var()[0]
print('Observed means :', read_data.groupby('version').mean().values.ravel())
print('Variance :', variance_observed)

def test_perm(temp_data):
    temp_data = temp_data.copy()
    temp_data['sum_gamerounds'] = np.random.permutation(temp_data['sum_gamerounds'].values)
    return temp_data.groupby('sum_gamerounds').mean().var()[0] # calculation of variance
variance_perm = [test_perm(read_data) for _ in range(3000)]

print('Pr(Prob) is', np.mean([x > variance_observed for x in variance_perm]))

# Using stats.f.oneway
f_value, p_value = stats.f_oneway(df['gate_30'],df['gate_40'])
print("Pvalue using stats.f.oneway function",p_value)
print("Fvalue using stats.f.oneway function",f_value)

# Derivation using F-stastic
mu=df.mean()
gmu=mu.mean()
print("Group wise mean of datas is ", mu.values)
print("Grand mean of data is ", gmu)

# Degree of freedom
degf=89398 # (total number element in a group -1)*number of groups ((44700-1)*2=89398)
gdegf=1 # total number of treatments -1 (2-1=1)

# Sum of Squares (SS) of error, group wise
var_temp=df-mu
var_temp=var_temp**2
var_temp=var_temp.sum().sum()
SS=1*var_temp
print("Sum of Squares (SS) of error, group wise: ",var_temp)

# Mean of Sum of squares of error group wise
MSS=SS/degf 
print("Mean of Sum of squares of error group wise: ",MSS)

# Sum of squares of error for whole data
GSS=((mu-gmu)**2).sum()*2
var_temp=(mu-gmu)**2
print("Sum of squares of error for whole data: ",GSS)

# Mean of Sum of squares of error group wise
GMSS=GSS/gdegf 
print("Mean of Sum of squares of error group wise: ",GMSS)

# Fvalue
F_value=GMSS/MSS
print("F_value: ",F_value)

def test_perm_2(temp_data):
    temp_data = temp_data.copy()
    temp_data['sum_gamerounds'] = np.random.permutation(temp_data['sum_gamerounds'].values)
    var_temp=temp_data.set_index("version")
    df=var_temp.loc["gate_30"].reset_index()
    df["gate_40"]=var_temp.loc["gate_40"].reset_index()["sum_gamerounds"]
    df["gate_30"]=var_temp.loc["gate_30"].reset_index()["sum_gamerounds"]
    df=df.iloc[:,5:]
    mu=df.mean()
    SS=((df-mu)**2).sum().sum()
    MSS=SS/degf
    GSS=((mu-gmu)**2).sum()*2
    GMSS=GSS/gdegf 
    F_value_perm=GMSS/MSS
    return F_value_perm
variance_perm = [test_perm_2(read_data) for _ in range(3000)]

print('Pr(Prob) is', np.mean([x > F_value for x in variance_perm]))


# Derivation using Anova table
model = ols("sum_gamerounds ~ version", data=read_data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)