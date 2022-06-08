'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 8
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

wh_data=pd.read_csv("weight-height.csv")
print(wh_data)
mean_population = round(wh_data['Height'].mean(),3)
print(f"mean_population: {mean_population}")

# ##############################
# ######### question 1 #########
# ##############################

# Perform Random Sampling by choosing 1000 samples from data. Compute the sample mean
# and population mean (from whole data) and then compute the error between both mean.

sample_random = wh_data.sample(n=1000).sort_index()
print(sample_random)

mean_sample=round(sample_random['Height'].mean(),3)
print(f"mean_sample: {mean_sample}")

output = {'mean_sample':[mean_sample],'mean_population':mean_population}
output = pd.DataFrame(output, index=['Simple Random Sampling'])     # Transform dictionary into a data frame
output['abs_error'] = abs(output['mean_population'] - output['mean_sample'])    # Add a value corresponding to the absolute error
output.sort_values(by='abs_error')  # Sort data frame by absolute error
print(output,end="\n\n")

# ##############################
# ######### question 2 #########
# ##############################

# Perform Systematic Sampling by choosing 1000 samples from data. Compute the sample
# mean and population mean (from whole data) and then compute the error between both mean.

def systematic_sampling(df, step):
    
    indexes = np.arange(0,1000,step=step)
    systematic_sample = df.iloc[indexes]
    return systematic_sample
    
systematic_sample = systematic_sampling(wh_data, 1)     # Obtain a systematic sample and save it in a new variable
mean_systematic = round(systematic_sample['Height'].mean(),3)   # Save the sample mean in a separate variable
print(systematic_sample)    # View sampled data frame

output2 = {'mean_systematic':[mean_systematic],'mean_population':mean_population}
output2 = pd.DataFrame(output2, index=[' Systematic Sampling'])   # Transform dictionary into a data frame
output2['abs_error'] = abs(output2['mean_population'] - output2['mean_systematic'])  # Add a value corresponding to the absolute error
output2.sort_values(by='abs_error')    # Sort data frame by absolute error
print(output2,end="\n\n")

# ##############################
# ######### question 3 #########
# ##############################

# Perform Stratified Sampling by choosing 1000 samples from data. Compute the sample mean
# and population mean (from whole data) and then compute the error between both mean.

split = StratifiedShuffleSplit(n_splits=1, test_size=1000)  # Set the split criteria
# print(split)

for x, y in split.split(wh_data, wh_data['Gender']):    # Perform data frame split
    stratified_random_sample = wh_data.iloc[y]

stratified_random_sample_mean = round(stratified_random_sample['Height'].mean(),3)  # View sampled data frame
print(stratified_random_sample)

output3 = {'mean_stratified':[stratified_random_sample_mean],'mean_population':mean_population}
output3 = pd.DataFrame(output3, index=[' Stratified Sampling'])   # Transform dictionary into a data frame
output3['abs_error'] = abs(output3['mean_population'] - output3['mean_stratified'])  # Add a value corresponding to the absolute error
output3.sort_values(by='abs_error')    # Sort data frame by absolute error
print(output3,end="\n\n")