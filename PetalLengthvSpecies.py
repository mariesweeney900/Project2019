import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
x = dataframe.petal_length
y = dataframe.species

plt.scatter(x, y)

plt.show()