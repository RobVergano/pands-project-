# bargraph.py
# This program creates a bar chart for the four attributes based on the average per class.
# Author: Roberto Vergano


from attr import attr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.svm import l1_min_c

ds = pd.read_csv("iris.csv")

setosa = ds[0:50]
versicolor = ds[50:100]
virginica = ds[100:150]

iris = [setosa,versicolor,virginica]

atm = [],[],[],[]

for i in iris:
    y = i["petal_length"].mean()
    atm[0].append(y)

for i in iris:
    y = i["petal_width"].mean()
    atm[1].append(y)

for i in iris:
    y = i["sepal_length"].mean()
    atm[2].append(y)

for i in iris:
    y = i["sepal_width"].mean()
    atm[3].append(y)

ats = [],[],[],[]

for i in iris:
    y = i["petal_length"].std()
    ats[0].append(y)

for i in iris:
    y = i["petal_width"].std()
    ats[1].append(y)

for i in iris:
    y = i["sepal_length"].std()
    ats[2].append(y)

for i in iris:
    y = i["sepal_width"].std()
    ats[3].append(y)

# PETAL LENGTH 
data = {"Iris setosa": atm[0][0],"Iris versicolor":atm[0][1],"Iris virginica":atm[0][2]}
type = list(data.keys())
values = list(data.values())
plt.bar(type,values,yerr=ats[0],color = "lightcoral",width =0.4)
plt.title("Petal length mean")
plt.ylabel("Petal length(cm)/sd")
plt.show()

# PETAL WIDTH
data1 = {"Iris setosa": atm[1][0],"Iris versicolor":atm[1][1],"Iris virginica":atm[1][2]}
type1 = list(data1.keys())
values1 = list(data1.values())
plt.bar(type1,values1,yerr=ats[1],color ="wheat", width=0.4)
plt.title("Petal width mean")
plt.ylabel("Petal width (cm)/sd")
plt.show()

# SEPAL LENGTH
data2 = {"Iris setosa": atm[2][0],"Iris versicolor":atm[2][1],"Iris virginica":atm[2][2]}
type2 = list(data2.keys())
values2 = list(data2.values())
plt.bar(type2,values2,yerr=ats[2],color ="lightsteelblue", width=0.4)
plt.title("Sepal length mean")
plt.ylabel("Sepal length(cm)/sd")
plt.show()

# SEPAL WIDTH
data3 = {"Iris setosa": atm[3][0],"Iris versicolor":atm[3][1],"Iris virginica":atm[3][2]}
type3 = list(data3.keys())
values3 = list(data3.values())
plt.bar(type3,values3,yerr=ats[3],color ="lightgreen", width=0.4)
plt.title("Sepal width mean")
plt.ylabel("Sepal width (cm)/sd")
plt.show()