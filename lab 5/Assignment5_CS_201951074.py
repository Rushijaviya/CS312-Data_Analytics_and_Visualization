'''
    Name: Javiya Rushi
    ID: 201951074
'''

# Assignment 5
import sys
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
from statsmodels.graphics.mosaicplot import mosaic
from joypy import joyplot  # !pip install joypy
import squarify  # pip install squarify
import plotly.express as exp  # pip install plotly

# ##############################
# ######### question 1 #########
# ##############################

# Present the information present in (”heart.csv”) as any two appropriate plots.

read = pd.read_csv("heart.csv")
read.head()


f = exp.parallel_categories(read, dimensions=['sex', 'cp',   'fbs',   'slope', 'ca', 'thal','target'], color="age", color_continuous_scale=exp.colors.sequential.Plasma)
f.show()

f2 = exp.treemap(read, path=["age", "cp"], values="target")
f2

f3 = sns.PairGrid(read[['age','trestbps', 'chol', 'thalach', 'oldpeak', 'slope',   'target']])
f3.map(sns.scatterplot)