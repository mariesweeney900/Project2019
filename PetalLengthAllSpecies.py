import pandas as pd
#imports pandas as pd
   
import matplotlib.pyplot as plot
#imports matplotlib as plt
   
dataframe = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
#Adapted from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
# read the data from the downloaded CSV file.


Setosa = dataframe.loc[dataframe['species'] == 'setosa']
Versicolor = dataframe.loc[dataframe['species'] == 'versicolor']
Virginica = dataframe.loc[dataframe['species'] == 'virginica']
#creates a dataframe of each species and asssigns them

number_of_samples = int(50)
#defines the number of samples and assigns them an integer

plot.scatter(range(number_of_samples),Setosa["petal_length"], color = "yellow")
plot.scatter(range(number_of_samples),Versicolor["petal_length"], color = "red")
plot.scatter(range(number_of_samples),Virginica["petal_length"], color = "blue")
#utilises the plot.scatter function in matplotlib to create a scatter plot, uses the range function to define y and number of samples, defines x axis as petal length of all species and assigns them their respective colours

plot.title("Petal Length Setosa, Versicolor and Virginica")
plot.xlabel('Number_Samples')
plot.ylabel('petal_length')

plot.show()
#uses the title label and show functions in matplotlib to give a title to the plot and label the x and y axis and then shows the plot