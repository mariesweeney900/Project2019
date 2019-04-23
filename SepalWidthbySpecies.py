import pandas as pd
#import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib as plt
dataframe = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
#creates a dataframe from csv file found at website address
#Adapted from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

x = dataframe.sepal_width
y = dataframe.species
#assigns variables x and y to sepal width and species
#Adapted from https://ourcodingclub.github.io/2018/04/18/pandas-python-intro.html

plt.xlabel("Sepal Width (cm)", fontsize=16)
plt.ylabel("Species", fontsize=16)
plt.scatter(x, y)
plt.show()
#applies labels sepal width and species of font size 16 to x and y axis
#creates a scatter plot of the data using the scatter function in matplotlib 
#shows the plot of the data using the show function
#Adapted from https://matplotlib.org/users/pyplot_tutorial.html
