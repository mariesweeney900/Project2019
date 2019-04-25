import pandas as pd
#imports pandas as pd

import matplotlib.pyplot as plt
#imports matplotlib as plt



data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv', index_col = 'species')
# read the data from the downloaded CSV file.

data.loc['versicolor'].plot()
#data. is an operation that locates rows that virginica is found

plt.ylabel("Measurements (cm)", fontsize=16)
#labels the y axis of the plot as Measurements in cm and applies fontsize of 16

plot.show()
#thia function in atplotlib shows the plot