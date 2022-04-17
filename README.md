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

**Figure 1. Summary of each variable.**

![alt text](https://github.com/RobVergano/pands-project-/blob/main/Screenshots%20from%20analysis.py/Summary%20of%20each%20variable.png)

In order to give a neat appearance to the results I decided to calculate separately the mean, standard deviation(std), max and min. 

First, creating a variable for the dataframe of each attribute.(7)

``
sl = ds["sepal_length"]
sw = ds["sepal_width"]  
pl = ds["petal_length"]
pw = ds["petal_width"]
``  

Then calculating the mean,std, max and min to up to 2 decimals (8)(9)(10)(11)  
``
slm = round((sl.mean()),2)
``
  
Using "format" (12) we output the results for the mean and std for each variable in a single sentence. Similar approach was used to calculate the max and min.  
  
**Figure 2. Summary of mean, std, max and min for each attribute.**    

![alt text](https://github.com/RobVergano/pands-project-/blob/main/Screenshots%20from%20analysis.py/meanstdmaxmin.png)

From this summary, we can observe that:  
1. On average, sepal length is bigger than petal length for the three species.
2. On average, sepal width is bigger than petal width for the three species.  

## 6.HISTOGRAM OF EACH VARIABLE  

With the histogram we are going to check how the values for each attribute are distributed between the range of the max and min. Thereby, we will be able to see how many times a certain value occurs within the max/min range.

In order to do that, we are going to import matplotlib module and the scatter matrix from pandas.(13)(14)

``
import matplotlib.pyplot as plt 
``  
``  
from pandas.plotting import scatter_matrix 
``  

Then we will use the "hist" function to create the histogram.(14)  
``
ds.hist(figsize=(12,8))
``

**Figure 3. Histogram of each variable.**

![alt text](https://github.com/RobVergano/pands-project-/blob/main/Histogram/Histogram.png)

The histogram shows a high variety in the values distribution, which it may be related to the differences among species.

## 7. SCATTER PLOT OF EACH PAIR OF VARIABLES

Scatter plots are used to observe relationship between variables. With the Pandas module we can create a matrix comparing each pair of attributes.(15)

``
pd.plotting.scatter_matrix(ds)
``

**Figure 4. Scatter plot of each pair of variables.**

![alt text](https://github.com/RobVergano/pands-project-/blob/main/Scatter%20plot%20figures/Scatter%20plot.png)


The scatter plot shows:  
1. Sepal length and petal length shows an uphill trend, but the relationship is not strong and inconclusive.  
2. There isa  positive relationship between sepal length and petal length. A potential linear progression is observed, however, the trend is weak.  
3. Petal length and petal width shows the strongest relationship, an uphill linear progression which it seems to be divided in two sections. 

Figure 5 shows the trendline between petal length and petal width.(16)

``
z = np.polyfit(pl, pw, 1)
``  
``
p = np.poly1d(z)
``  
``
plt.plot(pl,p(pl),"r--")
``  

**Figure 5. Scatter plot Petal length vs Petal width.**

![alt text](https://github.com/RobVergano/pands-project-/blob/main/Scatter%20plot%20figures/Petal%20length%20vs%20Petal%20width%20scatter%20plot.png)


**Conclusions from the attributes analysis:**  

1. The strongest relationship found among the attributes is petal length/petal width, showing that the length of the petal is proportional to petal width. The trend is divided in two sections, which it could be related to the differences among species.
2. Other attribute relationships are inconclusive.

The next steps in this analysis will be:

1. To observe how the different Iris species impact on the attributes.
2. To check if the relationship petal length/width is due to the Iris species.

## 8. DESCRIPTIVE ANALYSIS BY IRIS CLASS.

Since the dataset is organized by attributes, we will have to make sure we extract the data only by class.

For this task, we will have to slice the dataset by class. Knowing that we have 50 samples per class in the dataset, we can slice by class as follows.(17)

``
setosa = ds[0:50]
``  
``
versicolor = ds[50:100]
``  
``
virginica = ds[100:150]
``  




REFERENCES

(1) https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x  
(2) https://archive.ics.uci.edu/ml/datasets/iris  
(3) https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file  
(4) https://www.w3schools.com/python/pandas/pandas_csv.asp  
(5) https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/  
(6) https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html  
(7) https://pandas.pydata.org/docs/user_guide/indexing.html  
(8) https://www.w3schools.com/python/ref_func_round.asp  
(9) https://www.geeksforgeeks.org/python-statistics-mean-function/  
(10)https://www.geeksforgeeks.org/max-min-python/  
(11)https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html  
(12)https://www.edureka.co/blog/format-function-in-python/  
(13)https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html  
(14)https://matplotlib.org/3.5.0/gallery/statistics/hist.html  
(15)https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html  
(16)https://stackoverflow.com/questions/41635448/how-can-i-draw-scatter-trend-line-on-matplot-python-pandas  
(17)https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html





