# analysis.py
# Author: Roberto Vergano
# 
# ds = dataset
import pandas as pd
import numpy as np
from regex import F

f = open("summary of variables output.txt","a") 
ds = pd.read_csv("iris.csv")

# SUMMARY OF VARIABLES

print ("IRIS DATASET: DESCRIPTIVE ANALYSIS BY ATTRIBUTE", file = f)
print("\n", file = f)
print("NUMBER OF ROWS PER CLASS", file = f)
print("\n", file = f)
print(ds.groupby("class").size(), file = f)
print("\n", file = f)
print("SUMMATY OF VARIABLES", file = f)
print("\n", file = f)
print(ds.describe(), file =f)
print("\n", file = f)

sl = ds["sepal_length"]
sw = ds["sepal_width"]
pl = ds["petal_length"]
pw = ds["petal_width"]

slm = round((sl.mean()),2)
swm = round((sw.mean()),2)
plm = round((pl.mean()),2)
pwm = round((pw.mean()),2)

slsd = round((sl.std()),2)
swsd = round((sw.std()),2)
plsd = round((pl.std()),2)
pwsd = round((pw.std()),2)

print ("MEAN VALUES PER ATTRIBUTE", file = f)
print("\n", file = f)
print ("Sepal length mean (sd) = {} ({})".format(slm,slsd), file = f)
print ("Sepal width mean (sd) = {} ({})".format(swm,swsd), file = f)
print ("Petal length mean (sd) = {} ({})".format(plm,plsd), file = f)
print ("Petal width mean (sd) = {} ({})".format(pwm,pwsd), file = f)
print("\n", file = f)

slmax = sl.max()
swmax = sw.max()
plmax = pl.max()
pwmax = pw.max()

slmin = sl.min()
swmin = sw.min()
plmin = pl.min()
pwmin = pw.min()

print("MAX AND MIN VALUES PER ATTRIBUTE", file = f)
print("\n", file = f)
print ("Sepal length max/min values are: {}/{}".format(slmax, slmin), file = f)
print ("Sepal width max/min values are: {}/{}".format(swmax,swmin), file = f)
print ("Petal length max/min values are: {}/{}".format(plmax,plmin), file = f)
print ("Petal width max/min values are: {}/{}".format(pwmax,pwmin), file = f)
print("\n", file = f)

#HISTOGRAM OF EACH VARIABLE

import matplotlib.pyplot as plt 
from pandas.plotting import scatter_matrix 

ds.hist(figsize=(12,8))
plt.show()

# SCATTER PLOT OF EACH PAIR OF VARIABLES

pd.plotting.scatter_matrix(ds)
plt.show()

plt.scatter(pl,pw, c="green")
plt.title("Petal length vs Petal width")
plt.xlabel("Petal length (cm)")
plt.ylabel("Petal width (cm)")
plt.show()

# DESCRIPTIVE ANALYSIS BY CLASS

setosa = ds[0:50]
versicolor = ds[50:100]
virginica = ds[100:150]

print("DESCRIPTIVE ANALYSIS BY CLASS", file =f)
print("\n", file = f)
print("Iris setosa", file =f)
print("\n", file = f)
print(setosa.describe(),file=f)
print("\n", file = f)
print("Iris versicolor",file=f)
print("\n", file = f)
print(versicolor.describe(),file =f)
print("\n", file = f)
print("Iris virginica",file=f)
print("\n", file = f)
print(virginica.describe(),file=f)
print("\n", file = f)