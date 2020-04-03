import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
plt.style.use('seaborn-whitegrid')


# In scatter plots the inividual points are represented using symbols.

fig  =plt.figure()
ax = plt.axes()

x = np.linspace(0,10,30)
y = np.sin(x)



# third argument is the type of symbol used of plotting
# a few other types are '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd'
# s - square
# d - diamond
# v - reversed triangle

##plt.plot(x,y,'o',color = 'black')

# symbol, conneted with line segements and color together

##plt.plot(x,y,"-ok")

# Second way for plotting scatter plots is using scatter function.
#The primary difference of plt.scatter from plt.plot is that it can be used
# to create scatter plots where the properties of each individual point
# (size, face color, edge color, etc.) can be individually controlled or mapped to data.
# hence it is more efficient to use plot function for larger datasets to redure rendering work

##plt.scatter(x,y,marker='o')

# Lets see the difference in action suing the visualisation of Iris Dataset
iris = load_iris()
features = iris.data.T
plt.scatter(features[0],features[1],alpha=0.2,s= 100*features[3], c=iris.target ,cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.show()