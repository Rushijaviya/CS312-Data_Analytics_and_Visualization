'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 2
import pandas as pd
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt

# Task 1

dataset= pd.read_csv('JK-Allopathic-Outpatient_attendance-May-2019.csv')
# print(dataset)
dataset["Attendance"] = dataset["Total No. of Facilities #"]*dataset['Performance - Overall Average **']
#print(dataset["Attendance"])

# ##############################
# ######### question 1 #########
# ##############################

# Compute total patient attendance for all district for all four range group and plot the bar diagram. 
# Set the bar plot parameters for better visualization.

que_1 = dataset.groupby("District")["Attendance"].sum()
que_1=que_1.to_frame()
que_1.reset_index(inplace=True)
sns.set(rc={'figure.figsize':(8,8)})
sns.barplot(data=que_1,x="Attendance", y="District")

# ##############################
# ######### question 2 #########
# ##############################

# Compute total patient attendance for all district for each Facility Type (DH, CHC and SC) for
# all four range groups and plot the staked bar diagram of three. Set the bar plot parameters for
# better visualization.

que_2=dataset.pivot_table("Attendance",index="District",columns="Facility Type")
que_2.plot(kind='bar', stacked=True)

# ##############################
# ######### question 3 #########
# ##############################

# Plot group bar plot for Performance - Overall Average of different Facility Type (DH, CHC and
# SC) of Anantnag, Jammu, Poonch, Reasi and Udhampur.

index=dataset["District"].isin(["Anantnag","Jammu",'Poonch', 'Reasi','Udhampur'])
que_3=dataset[index]
ax=sns.barplot(data=que_3,x="Performance - Overall Average **",y="District",hue="Facility Type")
ax.set_xscale("log")

# ##############################
# ######### question 4 #########
# ##############################

# Present dot plot for Performance - Maximum of any 20 different district. Performance - Maximum 
# for different Facility Type should be combined appropriately using a aggregation function
# for each district.

que_4=dataset.groupby(["District"])['Performance - Maximum'].sum()
que_4=que_4.reset_index()
que_4=que_4.iloc[0:20]
sns.scatterplot(data=que_4, x="Performance - Maximum", y="District")

# Task 2

data=pd.read_csv('Fifa_player_football_data.csv')
# print(data)

# ##############################
# ######### question 1 #########
# ##############################

# Present Age of various football players as histogram and kernel density plots. Set appropriate
# parameters of the plot.

sns.histplot(data=data, x="Age", binwidth=1, color='b', kde=True)
sns.kdeplot(data=data, x="Age", color='g',fill=True)

# ##############################
# ######### question 2 #########
# ##############################

# Present Age of various Football players as Kernel Density plots for each of FC Barcelona, Chelsea,
# Juventus and Real Madrid Clubs. Set appropriate parameters of the plot.

index=data["Club"].isin(['Chelsea' ,'Real Madrid','FC Barcelona','Juventus'])
que_22=data[index]
sns.kdeplot(data=que_22, x="Age",hue='Club',fill=True)

# ##############################
# ######### question 3 #########
# ##############################

# Plot Value of players as Stacked Histogram Preferred Foot wise (right and left).

sns.histplot(data=data, x="Value",hue="Preferred Foot",multiple="stack")

# ##############################
# ######### question 4 #########
# ##############################

# Check distribution of International Reputation using Q-Q plot.

que_4=data['International Reputation']
qqplot(que_4,line='s')
plt.show()