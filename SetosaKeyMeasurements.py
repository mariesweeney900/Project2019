import pandas as pd
#imports pandas as pd

import matplotlib.pyplot as plt
#imports matplotlib as plt



data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv', index_col = 'species')
#Adapted from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
# read the data from the downloaded CSV file.

data.loc['setosa'].plot()
plt.ylabel("Measurements (cm)", fontsize=16)
plot.show()
#data.loc is an operation that locates rows that setosa is in
#labels the y axis of the plot as Measurements in cm and applies fontsize of 16
#thia function in matplotlib shows the plot
#Adapted from https://swcarpentry.github.io/python-novice-gapminder/09-plotting/?fbclid=IwAR1tJvpM5b2qMJVdFqk8AUy-tVN8JURNRrHt8N9scsRbjmb6rql_uwY-LUw
