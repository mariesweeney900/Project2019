import pandas as pd
#imports pandas as pd
import matplotlib.pyplot as plt
#imports matplotlib as plt

dataframe = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
#Adapted from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
# read the data from the downloaded CSV file.


dataframe.mode()
#Adapted from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html?fbclid=IwAR2b-doroozwxyDoBwdGYmITeDtGR7QlQAgNctS_xHWroMGz0GTfBtyR-7A
#gets the mode of the dataframe created
