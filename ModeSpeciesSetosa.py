import pandas as pd
#imports pandas as pd

import matplotlib.pyplot as plot
#imports matplotlib as plt

dataframe = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
#Adapted from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
# read the data from the downloaded CSV file.

Species1 = dataframe.loc[dataframe['species'] == 'setosa']
Species1.mode()
#Adapted from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html?fbclid=IwAR2b-doroozwxyDoBwdGYmITeDtGR7QlQAgNctS_xHWroMGz0GTfBtyR-7A
#makes a dataframe from the species setosa therby isolating it from other species and labelling it species1
# gets the mode of variable species1 