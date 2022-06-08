'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 10
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pylab as py
import statsmodels.api as sm

data = pd.read_csv('loan-train.csv')
data.head()

# ##############################
# ######### question 1 #########
# ##############################

# Plot the histogram of the Applicant’s Income.

data['ApplicantIncome'].hist()
plt.show()

sns.histplot(data['ApplicantIncome'])
plt.show()

columm = data['ApplicantIncome']

z = (columm - np.mean(columm))/np.std(columm)

print("Mean of the data: ",np.mean(z))
print("Standard deviation of the data: ",np.std(z))

sns.histplot(z,kde=True)
plt.show()

# ##############################
# ######### question 2 #########
# ##############################

# Check the distribution of Applicant’s Income is a Normal Distribution or not using QQ plot.

sm.qqplot(z, line ='45')
py.show()