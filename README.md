# IRIS DATASET PROJECT

## 1.PROJECT OBJECTIVES

1. Research the dataset online and write a summary about it in your README.
2. Download the dataset and add it to the repository.
3. Write a program called analysiss.py that:
    1. Outputs a summary of each variable to a single txt file.
    2. Saves a histogram of each variable to png files, and
    3. Outputs a scatter plot of each pair of variables.
4. Performs any other analysis you think is appropriate.

The aim of this project is to apply the knowledge acquired through the module into the iris database. 
First, analysing the four variables to see if there is any relationship between them.
Secondly, if a relationship is found, how it compares with the different classes. 

## 3. SOFTWARE USED.

Visual studio Code.  
Git Hub.

## 4. INTRODUCTION

Introduced by Ronald Fisher in his paper "The use of multiple measurements in taxonomic problems", it includes three iris species with 50 samples each and also some properties about each flower.(1)

The three classes in the data set are the Iris Setosa, the Iris Versicolor and the Iris Virginica.(1)

The attributes described in the dataset are: 
  1. sepal length in cm
  2. sepal width in cm
  3. petal length in cm
  4. petal width in cm
  5. class: Iris Setosa, Iris Versicolor and Iris Virginica.(2)

Based on these attributes, Fisher developed a linear discriminant analysis where the species can be differenciated from each other.(1)(2)

## 5. SUMMARY OF EACH VARIABLE.

The Iris database was downloaded (2) and added to the Pands-project repository.

For the first task, I created a text file (3) where the summary of the variables will go.  

``  
f = open("summary of variables output.txt","a")
``

Then, using the pandas module, the "ds" variable will read the iris database and we will be able to extract the data required. (4)

``
ds = pd.read_csv("iris.csv")
``

Using "groupby", we will check whether the dataset contains 50 samples per class as referenced at the introduction and save it into the text file.(5)

``
print(ds.groupby("class").size(), file = f)
``

To obtain a summary of the variables we will use "describe", which generates a descriptive stadistic analysis of the mean, standard deviation, max, min and percentiles.(6)

``
print(ds.describe(), file =f)
``

Figure 1. Summary of each variable.

![alt text](https://github.com/RobVergano/pands-project-/blob/main/Screenshots%20from%20analysis.py/Summary%20of%20each%20variable.png)

In order to give a neat appearance to the results I decided to calculate separately the mean, standard deviation, max and min. 

First, creating a variable for the dataframe of each attribute.(7)

``
sl = ds["sepal_length"]``
sw = ds["sepal_width"]``
pl = ds["petal_length"]``
pw = ds["petal_width"]``
``






References

(1) https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x  
(2) https://archive.ics.uci.edu/ml/datasets/iris  
(3) https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file  
(4) https://www.w3schools.com/python/pandas/pandas_csv.asp  
(5) https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/  
(6) https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html  
(7) https://pandas.pydata.org/docs/user_guide/indexing.html

