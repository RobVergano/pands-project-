
from cProfile import label
from re import A
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

ds = pd.read_csv("iris.csv")

setosa = ds[0:50]
versicolor = ds[50:100]
virginica = ds[100:150]

iris = (setosa, versicolor, virginica)

mean_sepallenght = []

def sepallenght(iris):
    for x in iris:
        y = x["sepal_length"].mean()
        mean_sepallenght.append(y)
    return mean_sepallenght 
a = sepallenght(iris)

std_sepallenght = []

def stdsepallenght(iris):
    for x in iris:
        y = x["sepal_length"].std()
        std_sepallenght.append(y)
    return std_sepallenght
a_std = stdsepallenght (iris) 

mean_sepal_width = []

def sepalwidth(iris):
    for x in iris:
         y = x["sepal_width"].mean()
         mean_sepal_width.append(y)
    return mean_sepal_width
b = sepalwidth(iris)

std_sepal_width = []

def stdsepalwidth(iris):
    for x in iris:
        y = x["sepal_length"].std()
        std_sepal_width.append(y)
    return std_sepal_width
b_std = stdsepalwidth(iris)

mean_petal_length = []

def petallength(iris):
    for x in iris:
        y = x["petal_length"].mean()
        mean_petal_length.append(y)
    return mean_petal_length
c = petallength(iris)

std_petal_length = []

def stdpetallength(iris):
    for x in iris:
        y = x["petal_length"].std()
        std_petal_length.append(y)
    return std_petal_length

c_std = stdpetallength(iris)

mean_petal_width = []

def petalwidth(iris):
    for x in iris:
        y = x["petal_width"].mean()
        mean_petal_width.append(y)
    return mean_petal_width
d = petalwidth(iris)

std_petal_width = []

def stdpetalwidth(iris):
    for x in iris:
        y = x["petal_width"].std()
        std_petal_width.append(y)
    return std_petal_width
d_std = stdpetalwidth (iris)

data = {"Iris setosa":a[0],"Iris versicolor":a[1], "Iris virginica":a[2]}
type = list(data.keys())
values = list(data.values())
sd = list(a_std)
plt.bar(type,values,yerr=sd,color = "lightsteelblue",width =0.4)
plt.title("Sepal length mean")
plt.ylabel("Sepal length(cm)/sd")
plt.show()

data2 = {"Iris setosa":b[0],"Iris versicolor":b[1],"Iris virginica":b[2]}
type2 = list(data2.keys())
values2 = list(data2.values())
sd2 = list(b_std)
plt.bar(type2, values2,yerr=sd2,color="lightgreen", width=0.4)
plt.title("Sepal width mean")
plt.ylabel("Sepal width (cm)/sd")
plt.show()

data3 = {"Iris setosa":c[0],"Iris versicolor":c[1],"Iris virginica":c[2]}
type3 = list(data3.keys())
values3 = list (data3.values())
sd3 = list(c_std)
plt.bar(type3, values3,yerr=sd3,color="lightcoral", width=0.4)
plt.title("Petal length mean")
plt.ylabel("Petal length (cm)/sd")
plt.show()

data4 = {"Iris setosa":d[0],"Iris versicolor":d[1],"Iris virginica":d[2]}
type4 = list(data4.keys())
values4 = list(data4.values())
sd4 = list(d_std)
plt.bar(type4, values4,yerr=sd4,color="wheat", width=0.4)
plt.title("Petal width mean")
plt.ylabel("Petal width (cm)/sd")
plt.show()