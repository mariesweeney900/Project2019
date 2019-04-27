import pandas as pd
#imports pandas as pd

import matplotlib.pyplot as plot
#imports matplotlib as plt

dataframe = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
#Adapted from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
# read the data from the downloaded CSV file.

dataframe.describe()
#uses the describe function get retrieve summary statistics of the dataframe