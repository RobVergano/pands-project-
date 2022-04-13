#
#
#

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

columns_pl = [setosa_pl,versicolor_pl,virginica_pl]
columns_pw = [setosa_pw,versicolor_pw,virginica_pw]

fig1, ax = plt.subplots()
ax.boxplot(columns_pl, patch_artist= True,)
plt.xticks([1,2,3],["Iris setosa","Iris versicolor","Iris virginica"])
plt.ylabel("Petal length (cm)")
fig2, ax = plt.subplots()
ax.boxplot(columns_pw, patch_artist=True )
plt.xticks([1,2,3],["Iris setosa","Iris versicolor","Iris virginica"])
plt.ylabel("Petal width (cm)")
plt.show()


