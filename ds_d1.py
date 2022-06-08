# -*- coding: utf-8 -*-
"""DS D1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wMs8pWWMvtDa8hy6xu_rD4qvTnrW4Hq3

#Artificial Intelligence
Any technique which enables computers to mimic human behavior.
#Machine Learning
Subset of AI techniques which use statistical methods to enable machines to improve with experiences.
#Deep Learning
Subset of ML which make the computation of multilayer networks feasible.
#Data Science
Data science is a multi-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data.

#Data Preprocessing
Preprocessing refers to the transformation applied to our data before feeding it to ML algorithm.
Data Preprocessing is a technique that is used to convert the raw data into a clean data set.

#Numpy
Manipulating numerical data, similar to MATLAB. multi-dimensional arrays and matrices, along with a large collection of high level mathematical function to operate on these arrays.

#Pandas
For Data manipulation, cleaning and analysis,

#Matplotlib
For plotting data, or visualizing the analysis.

#Data Proprocessing
"""

from google.colab import drive
drive.mount("/content/drive")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/content/drive/MyDrive/Datasets (1)/titanic.csv")
df

from sklearn.impute import SimpleImputer

sample = df[df['GSM'].notna()]
sample=sample.iloc[-7:-1,[-3,-1]]
sample

imputer1 = SimpleImputer(missing_values=np.nan,strategy="mean")
imputer = imputer1.fit(sample)
sample1 = imputer.transform(sample)
sample1

sample = df[df['GSM'].notna()]
sample=sample.iloc[-10:-1,[-3,-1]]
sample

imputer2 = SimpleImputer(missing_values=np.nan,strategy="median")
imputer = imputer2.fit(sample)
sample2 = imputer.transform(sample)
sample2

sample = df[df['GSM'].notna()]
sample=sample.iloc[-15:-10,[-3,-1]]
sample

imputer3 = SimpleImputer(missing_values=np.nan,strategy="most_frequent")
imputer = imputer3.fit(sample)
sample3 = imputer.transform(sample)
sample3

df2 = pd.read_csv("/content/drive/MyDrive/Datasets (1)/2013-2017_School_Math_Results_-_Gender (1).csv")

df2.head()

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
df2.iloc[:,0]=LE.fit_transform(df2.iloc[:,0])

df2.head()

df2.iloc[:,[1,4]]=imputer2.fit_transform(df2.iloc[:,[1,4]])

df2.head()

from sklearn.preprocessing import OneHotEncoder

OHE = OneHotEncoder()

df3 = pd.read_csv("/content/drive/MyDrive/Datasets (1)/2013-2017_School_Math_Results_-_Gender (1).csv")

df3.head()

imputer2=SimpleImputer(missing_values=np.nan,strategy="most_frequent")
df3.iloc[:,4]=imputer2.fit_transform(pd.DataFrame(df3.iloc[:,4]))
imputer3=SimpleImputer(missing_values=np.nan,strategy="median")
df3.iloc[:,1:4]=imputer3.fit_transform(df3.iloc[:,1:4])

df3

dff=pd.DataFrame(OHE.fit_transform(df3[['Gender']]).toarray())
df3 = df3.join(dff)
df3=df3.iloc[:,1:]
df3

from sklearn.model_selection import train_test_split

x=df3.iloc[:,[0,1,2,4,5]]
y=df3.iloc[:,3]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

x_train.shape

