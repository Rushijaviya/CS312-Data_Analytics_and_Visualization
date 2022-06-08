'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 11
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

data = pd.read_csv('cookie_cats.csv')
print(data.head())

# ##############################
# ######### question 1 #########
# ##############################

# Check which version of the game is better by computing average ”sum gamerounds”.

ax = data.boxplot(by='version', column='sum_gamerounds')
ax.set_xlabel('')
ax.set_ylabel('sum_grounds')
plt.suptitle('')
plt.show()

mean_gate30=data[data['version']=='gate_30'].sum_gamerounds.mean()
mean_gate40=data[data['version']=='gate_40'].sum_gamerounds.mean()
print(mean_gate30)
print(mean_gate40)

diff=mean_gate30-mean_gate40
print(diff)

# ##############################
# ######### question 2 #########
# ##############################

# To check that the difference in average of ”sum gamerounds” is by change or it is real difference,
# perform the permutation Resampling on the data and derive the probability. Make the decision
# based on derived probability.

ngate_30=(data[data['version']=='gate_30']).shape[0]
print(ngate_30)
ngate_40=(data[data['version']=='gate_40']).shape[0]
print(ngate_40)

def perm_fun(x, nA, nB):
    n = nA + nB
    idx_B = set(random.sample(range(n), nB))
    idx_A = set(range(n)) - idx_B
    return x.loc[idx_B].mean() - x.loc[idx_A].mean()
perm_diffs = [perm_fun(data.sum_gamerounds, ngate_30, ngate_40) for _ in range(1000)]

fig, ax = plt.subplots(figsize=(5, 5))
ax.hist(perm_diffs, bins=11, rwidth=0.9)
ax.axvline(x = mean_gate30 - mean_gate40, color='black', lw=2)
ax.text(0.5, 180, 'Observed\ndifference',bbox={'facecolor':'white'})
ax.set_xlabel('Difference of sum_gamerounds')
ax.set_ylabel('Frequency')
plt.show()

a=[]
for i in range(len(perm_diffs)):
    if(perm_diffs[i] >mean_gate30 - mean_gate40):
      a.append(perm_diffs[i])
print(np.mean(a))