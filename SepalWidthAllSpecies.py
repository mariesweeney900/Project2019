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

plot.scatter(range(number_of_samples),Setosa["sepal_width"], color = "yellow")
plot.scatter(range(number_of_samples),Versicolor["sepal_width"], color = "red")
plot.scatter(range(number_of_samples),Virginica["sepal_width"], color = "blue")
#utilises the plot.scatter function in matplotlib to create a scatter plot, uses the range function to define y and number of samples, defines x axis as sepal width of all species and assigns them their respective colours

plot.title("Sepal Width Setosa, Versicolor and Virginica")
plot.xlabel('Number_Samples')
plot.ylabel('Sepal_Width')

plot.show()
#uses the title label and show functions in matplotlib to give a title to the plot and label the x and y axis and then shows the plot