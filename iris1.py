import numpy
#import numpy
import pandas
#import pandas
import sklearn
#import sklearn
data = numpy.genfromtxt('data\iris.csv',delimiter=',')
#attempted to read csv file from stored file but ran in to too many issues
data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
#assigned data to read csv from online file downloaded to computer and worked much better
AvData = numpy.mean(data[:,1])
#gets the mean of the data from column one
data.describe()
#gets the count, mean, standard deviation, minimum, max ad certain percentages of the data at 50, 25 and 75% of all columns of data as column 4 is string data it is not a number (nan)
data.describe().transpose()
#transposes the data as not all data is numerical isolating the column that can not be summarised
sepalmax=numpy.max(data[0,1])
sepalmax=numpy.max(data[1,1])
sepalmax=numpy.max(data[1,:])
sepalmax=numpy.max(data[1,0])
sepalmax=numpy.max(data[:,2])
sepalmax=numpy.max(data[:,0])
#attemted to get the max of data
df= pd.DataFrame(data)
#creates a dataframe of the data
maxsepal = dataframe.idmax(0,True)
maxsepal = pd.dataframe.idmax(0,True)
maxsepal = pd.Datframe.idmax(0,True)
maxsepal = Dataframe.idmax(0,True)
maxsepal = pd.Dataframe.idxmax(0,True)
# attempted to get the max length of the data column sepal length in column one







