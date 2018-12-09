import numpy as np
import pandas as pd

data = pd.read_csv('arrhythmia.data.txt', sep=",", header=None)


data.drop(data.columns[169:279],axis=1,inplace=True)
data.drop(data.columns[27:168],axis=1,inplace=True)


data.dropna(inplace=True)
data.drop_duplicates(inplace=True)


data.columns=["Age","Sex","Height","Weight","QRS duration","P-R","Q-T","T","P","aQRS","aT","aP","aQRST","J","Heart Rate",
              "wQ","wR","wS","wR'","wS'","Number of intrinsic deflections","Existence of ragged R wave","Existence of diphasic derivation of R wave",
             "Existence of ragged P wave","Existence of diphasic derivation of P wave","Existence of ragged T wave","Existence of diphasic derivation of T wave",
             "QRSA","QRSTA"]



data["diagnosis"]=data["Existence of ragged R wave"]+data["Existence of ragged P wave"]+data["Existence of ragged T wave"]
+data["Existence of diphasic derivation of P wave"]+data["Existence of diphasic derivation of R wave"]+data["Existence of diphasic derivation of T wave"]

data.drop()
import pyod
from sklearn.model_selection import train_test_split

Y_data=data.iloc[:,-1]
X_data=data.iloc[:,:-1]

X_train, X_test, y_train, y_test = train_test_split(X_data,Y_data,test_size=0.33, random_state=42)
from pyod.models.knn import KNN


clf_name = 'KNN'
clf = KNN()
clf.fit(X_train)

# get the prediction label and outlier scores of the training data
y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
y_train_scores = clf.decision_scores_  # raw outlier scores

# get the prediction on the test data
y_test_pred = clf.predict(X_test)  # outlier labels (0 or 1)
y_test_scores = clf.decision_function(X_test)  # outlier scores