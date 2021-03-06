# -*- coding: utf-8 -*-
"""DS_D11_SVM_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NBpRSKqPB3lw0jBNDlyERVZVLWd7cMxX
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("insurance.csv")

df.head(2)

x = df.iloc[:,[0,1,2,3,5,6]]
y = pd.DataFrame(df.iloc[:,4])

from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler

x.head(2)

sc = StandardScaler()
le = LabelEncoder()
ohe = OneHotEncoder()

x.iloc[:,[0,2,5]] = sc.fit_transform(pd.DataFrame(x.iloc[:,[0,2,5]]))

dff=pd.DataFrame(ohe.fit_transform(x.iloc[:,[1,4]]).toarray())
x = x.join(dff)

x.head(2)

x.drop(x.columns[[1,4]],axis=1,inplace=True)

x.head(2)

y = le.fit_transform(y)

from sklearn.model_selection import train_test_split

xtr,xte,ytr,yte = train_test_split(x,y,test_size=0.3)

from sklearn.svm import SVC

model = SVC(kernel="linear",random_state=0)

model.fit(xtr,ytr)

ypred = model.predict(xte)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(yte,ypred)

cm

from sklearn.metrics import accuracy_score

acs = accuracy_score(yte,ypred)

acs

from sklearn.metrics import plot_confusion_matrix

plot_confusion_matrix(model,xte,yte)

model.score(xte,yte)

