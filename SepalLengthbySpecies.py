import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
#Adapted from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

x = dataframe.sepal_length
y = dataframe.species

#Adapted from https://ourcodingclub.github.io/2018/04/18/pandas-python-intro.html

plt.xlabel("Sepal Length (cm)", fontsize=20)
plt.ylabel("Species", fontsize=20)

plt.scatter(x, y)

plt.show()

#Adapted from https://matplotlib.org/users/pyplot_tutorial.html
