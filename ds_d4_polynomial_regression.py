# -*- coding: utf-8 -*-
"""DS_D4_Polynomial_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MwSTk_tvWPvliWRW-cjUMRiLyUcRnnSp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("heart.csv")

df.head()

x1 = pd.DataFrame(df.iloc[:,0])
y1 = pd.DataFrame(df.iloc[:,7])
x2 = df.iloc[:,[0,3,4]]
y2 = pd.DataFrame(df.iloc[:,7])

from sklearn.preprocessing import PolynomialFeatures

poly2 = PolynomialFeatures(degree = 2)
poly3 = PolynomialFeatures(degree = 3)
poly4 = PolynomialFeatures(degree = 4)

x1

x1_poly2 = poly2.fit_transform(x1)
x1_poly3 = poly3.fit_transform(x1)
x1_poly4 = poly4.fit_transform(x1)

print(x1_poly2,x1_poly3,x1_poly4)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

reg1 = LinearRegression()
xtr1,xte1,ytr1,yte1 = train_test_split(x1,y1)
plt.scatter(xtr1,ytr1)
xtr1 = poly2.fit_transform(xtr1)
reg1.fit(xtr1,ytr1)
plt.scatter(xte1,reg1.predict(poly2.fit_transform(xte1)))

reg2 = LinearRegression()
xtr1,xte1,ytr1,yte1 = train_test_split(x1,y1)
plt.scatter(xtr1,ytr1)
xtr1 = poly3.fit_transform(xtr1)
reg2.fit(xtr1,ytr1)
plt.scatter(xte1,reg2.predict(poly3.fit_transform(xte1)))

reg3 = LinearRegression()
xtr1,xte1,ytr1,yte1 = train_test_split(x1,y1)
plt.scatter(xtr1,ytr1)
xtr1 = poly4.fit_transform(xtr1)
reg3.fit(xtr1,ytr1)
plt.scatter(xte1,reg3.predict(poly4.fit_transform(xte1)))

reg4 = LinearRegression()
xtr2,xte2,ytr2,yte2=train_test_split(x2,y2)
xtr2 = poly4.fit_transform(xtr2)
reg4.fit(xtr2,ytr2)

y_pred=reg4.predict(poly4.fit_transform(xte2))

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

print(mean_absolute_error(yte2,y_pred))
print(mean_squared_error(yte2,y_pred))
print(r2_score(yte2,y_pred))
