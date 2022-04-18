# boxplot.py
# this program creates a boxplot based on petal length and petal width by class.
# Author: Roberto Vergano

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

ds = pd.read_csv("iris.csv")

setosa = ds[0:50]
versicolor = ds[50:100]
virginica = ds[100:150]

setosa_pl = setosa["petal_length"]
setosa_pw = setosa["petal_width"]

versicolor_pl = versicolor["petal_length"]
versicolor_pw = versicolor["petal_width"]

virginica_pl = virginica["petal_length"]
virginica_pw = virginica["petal_width"]

setosa_sl = setosa["sepal_length"]
setosa_sw = setosa["sepal_width"]

versicolor_sl = versicolor["sepal_length"]
versicolor_sw = versicolor["sepal_width"]

virginica_sl = virginica["sepal_length"]
virginica_sw = virginica["sepal_width"]


columns_pl = [setosa_pl,versicolor_pl,virginica_pl]
columns_pw = [setosa_pw,versicolor_pw,virginica_pw]
columns_sl = [setosa_sl,versicolor_sl,virginica_sl]
columns_sw = [setosa_sw,versicolor_sw,virginica_sw]

fig1, ax = plt.subplots()
ax.boxplot(columns_pl, patch_artist= True,)
plt.xticks([1,2,3],["Iris setosa","Iris versicolor","Iris virginica"])
plt.ylabel("Petal length (cm)")
plt.title("Petal length per class")

fig2, ax = plt.subplots()
ax.boxplot(columns_pw, patch_artist=True )
plt.xticks([1,2,3],["Iris setosa","Iris versicolor","Iris virginica"])
plt.ylabel("Petal width (cm)")
plt.title("Petal width per class")

fig3, ax = plt.subplots()
ax.boxplot(columns_sl, patch_artist=True )
plt.xticks([1,2,3],["Iris setosa","Iris versicolor","Iris virginica"])
plt.ylabel("Sepal length (cm)")
plt.title("Sepal length per class")

fig4, ax = plt.subplots()
ax.boxplot(columns_sw, patch_artist=True )
plt.xticks([1,2,3],["Iris setosa","Iris versicolor","Iris virginica"])
plt.ylabel("Sepal width (cm)")
plt.title("Sepal width per class")

plt.show()


