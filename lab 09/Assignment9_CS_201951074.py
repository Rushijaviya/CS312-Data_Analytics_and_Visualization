'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 9
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv('weight-height.csv')['Height']
# print(data.head())

# ##############################
# ######### question 1 #########
# ##############################

# Verify the Central Limit Theorem using ”Height” feature of the data.

plt.hist(data, bins=200)
plt.show()
error_standard = np.std(data)/(np.sqrt(len(data)))
print(error_standard)

data_sample = np.random.choice(data,100,replace=False)
plt.hist(data_sample,bins=10)
plt.show()
error_standard = np.std(data_sample)/np.sqrt(len(data_sample))
print(error_standard)

number_of_samples=10000
size_of_sample=100
mean_sample=[]
for i in range(number_of_samples):
    mean_sample.append(np.mean(np.random.choice(data,size_of_sample,replace=False)))

plt.hist(mean_sample,bins=100)
plt.show()
error_standard=np.std(mean_sample)/np.sqrt(len(mean_sample))
print(error_standard)

# ##############################
# ######### question 2 #########
# ##############################

# Perform the Bootstrap on ”Height” feature of the data.

number_of_samples=10000 # R times
size_of_sample=300  # n
mean_sample=[]
for i in range(number_of_samples):
    # Calulate mean for n samples
    mean_sample.append(np.mean(np.random.choice(data,size_of_sample,replace=True)))

plt.hist(mean_sample,bins=100)
plt.show()
error_standard=np.std(mean_sample)/np.sqrt(len(mean_sample))
print(error_standard)

# ##############################
# ######### question 3 #########
# ##############################

# Calculate the Confidence Interval of 95 % using sample means derived using Bootstrap

CI=0.95
sorted_means=np.sort(mean_sample)
l=len(sorted_means)
idx=math.floor(l*((1-CI)/2))

print("Lower level :", sorted_means[idx])
print("Upper level :", sorted_means[l-idx-1])