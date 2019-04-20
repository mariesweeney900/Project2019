import numpy
#
import pandas
import sklearn
data = numpy.genfromtxt('data\iris.csv',delimiter=',')
AvData = numpy.mean(data[:,1])
data.describe()
sepalmax=numpy.max(data[0,1])
sepalmax=numpy.max(data[1,1])
sepalmax=numpy.max(data[1,:])
sepalmax=numpy.max(data[1,0])
sepalmax=numpy.max(data[:,2])
sepalmax=numpy.max(data[:,0])
df= pd.DataFrame(data)
maxsepal = dataframe.idmax(0,True)
maxsepal = pd.dataframe.idmax(0,True)
maxsepal = pd.Datframe.idmax(0,True)
maxsepal = Dataframe.idmax(0,True)
maxsepal = pd.Dataframe.idxmax(0,True)
df.idxmax(axis =1, skipna = True)
df.idxmax(axis = 0, skipna =True)






