#!F:\Other_Py\python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

############

print ("Content-Type: text/html")
print ("")
import cgi,cgitb

##########

list_products=['Alienware 15','Alienware 17','Dell 22 Monitor - P2219H','Dell PowerEdge R440 Rack Server','Dell PowerEdge T30 Server']
dataset=pd.read_csv("C:\\Users\\MUJ\\Desktop\\TO\\data2.csv",encoding = "ISO-8859-1")

for i in list_products:
    product=i
    dataset2=dataset.loc[(dataset['Product Type'] ==product)]
    dataset3=dataset2.groupby('Gender',as_index=False).count()
    dataset3=dataset3[['Gender','Customer Id']]
    dataset3=dataset3.rename(columns = {'Customer Id':'Pieces Sold'})

    X = dataset3.iloc[:, [0,1]].values

    index = np.arange(len(X[:,0]))
    plt.bar(index, X[:,1])
    plt.xlabel('Gender')
    plt.ylabel('Units Sold')
    plt.xticks(index, X[:,0])
    plt.title("Gender Wise Distribution of Units Sold of "+product)
    plt.show()

    
