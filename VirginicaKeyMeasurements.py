import pandas as pd
#imports pandas as pd

import matplotlib.pyplot as plt
#imports matplotlib as plt



data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv', index_col = 'species')
#Adapted from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
# read the data from the downloaded CSV file.

data.loc['virginica'].plot()
plt.ylabel("Measurements (cm)", fontsize=16)
plot.show()
#This is an operation  in matplotlib that locates rows that virginica is found
#labels the y axis of the plot as Measurements in cm and applies fontsize of 16
#this functionshows the plot
#Adapted from 'https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv'
