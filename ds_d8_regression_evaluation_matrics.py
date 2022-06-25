# -*- coding: utf-8 -*-
"""DS_D8_Regression_Evaluation_Matrics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zJ2tyAN_dFlyGSIruwjdriNyHBFbG8BL
"""

import numpy as np
import pandas as pd

df=pd.read_csv("train.csv")

df.dropna(inplace=True)
df=df.iloc[1:10,:]
df

"""#Standard Deviation
Standard deviation is a measure of how spread out numbers are. It can be calculated by taking square root of Variance.
#Variance
The variance is defined as :

The average of the squared differences from the Mean.

1. Calculate Mean.
2. Subtract mean from each number and square the result.
3. Take average of those numbers.

"""

x = df.iloc[:,0]
y = df.iloc[:,1]
x

mean = sum(x)/len(x)
mean

diff = x-mean
diff

sq = diff**2
sq

variance = sum(sq)/len(sq)
variance

import statistics as st

st.pvariance(x)

st.variance(x)

from math import sqrt
standev = sqrt(variance)
standev

st.pstdev(x)

st.stdev(x)

from sklearn.metrics import explained_variance_score
from sklearn.metrics import max_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score

explained_variance_score(x,y)

max_error(x,y)

"""#Mean Absolute Error"""

df["Diff"]=abs(x-y)
df

MAE=sum(df["Diff"])/len(df)
MAE

mean_absolute_error(x,y)

"""#Mean Squared Error"""

df["Sq"]=df["Diff"]**2
df

MSE = sum(df.Sq)/len(df)
MSE

mean_squared_error(x,y)

"""#Root Mean Squared Error"""

RMSE = sqrt(MSE)
RMSE

"""#Mean Squared Log Error"""

from math import log

df["X+1"]=x+1
df["Y+1"]=y+1
df["LogX"]=np.log(df["X+1"])
df["LogY"]=np.log(df["Y+1"])
df["Error"]=df.LogX-df.LogY
df["SqEr"]=df.Error**2
df

MSLE = sum(df.SqEr)/len(df)
MSLE

mean_squared_log_error(x,y)

