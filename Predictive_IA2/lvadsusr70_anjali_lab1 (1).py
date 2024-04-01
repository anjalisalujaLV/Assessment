# -*- coding: utf-8 -*-
"""LVADSUSR70_Anjali_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gYjsu7t8X8_dcFwIKLrS_08sRO6F6AeR
"""

import pandas as pd
data=pd.read_csv("/content/winequality-red.csv")
data.head(5)

data["quality"].value_counts()

data.isnull().sum()

data.shape

data.info()

data.describe()

from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy="mean")
data["fixed acidity"]=imp.fit_transform(data[["fixed acidity"]])
data["volatile acidity"]=imp.fit_transform(data[["volatile acidity"]])
data["citric acid"]=imp.fit_transform(data[["citric acid"]])
data["residual sugar"]=imp.fit_transform(data[["residual sugar"]])
data["sulphates"]=imp.fit_transform(data[["sulphates"]])
data["chlorides"]=imp.fit_transform(data[["chlorides"]])
data["free sulfur dioxide"]=imp.fit_transform(data[["free sulfur dioxide"]])
data.head()

data.isnull().sum()

data.duplicated().sum()

data.drop_duplicates(inplace=True)

data.duplicated().sum()

data.shape

data["quality"].value_counts()

l=list(data["quality"])
for i in range(len(data)):
  if l[i]>=3 and l[i]<=6:
    l[i]=0
  else:
    l[i]=1

data["quality"]=l

data.head()

data["quality"].value_counts()

plt.figure(figsize=(12,7))
sns.boxplot(data)
plt.show()

import numpy as np
from scipy.stats import zscore
threshold = 3.0
z_scores = zscore(data)
outliers = np.abs(z_scores) > threshold
data = data[~outliers]

data.isnull().sum()

from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy="mean")
data["fixed acidity"]=imp.fit_transform(data[["fixed acidity"]])
data["volatile acidity"]=imp.fit_transform(data[["volatile acidity"]])
data["citric acid"]=imp.fit_transform(data[["citric acid"]])
data["residual sugar"]=imp.fit_transform(data[["residual sugar"]])
data["sulphates"]=imp.fit_transform(data[["sulphates"]])
data["chlorides"]=imp.fit_transform(data[["chlorides"]])
data["free sulfur dioxide"]=imp.fit_transform(data[["free sulfur dioxide"]])
data["total sulfur dioxide"]=imp.fit_transform(data[["total sulfur dioxide"]])
data["density"]=imp.fit_transform(data[["density"]])
data["pH"]=imp.fit_transform(data[["pH"]])
data["alcohol"]=imp.fit_transform(data[["alcohol"]])
data.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12,7))
sns.heatmap(data.corr(),cmap="viridis",annot=True)
plt.show()

sns.pairplot(data,y_vars="quality")

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
X=data.drop(columns='quality') #feature
y=data["quality"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
st_x= StandardScaler()
X_train= st_x.fit_transform(X_train)
X_test= st_x.transform(X_test)
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
prediction=model.predict(X_test)
from sklearn.metrics import accuracy_score,classification_report
score=accuracy_score(y_test,prediction)
print("Accuracy_score:",score*100)

print("Classification Report:",classification_report(y_test,prediction))

from sklearn.model_selection import cross_val_score
error_rate = []

for i in range(1,40):

    knn = KNeighborsClassifier(n_neighbors=i)
    score = cross_val_score(knn, X, y, cv=10)
    error_rate.append(1-score.mean())

plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, color='yellow', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)

from sklearn.metrics import confusion_matrix
knn = KNeighborsClassifier(n_neighbors=17)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print("Accuracy score",accuracy_score(y_test,pred))
print("Classification Matrix:",classification_report(y_test, pred))
print("confusion_matrix")
sns.heatmap(confusion_matrix(y_test, pred),annot=True,cmap="viridis")

