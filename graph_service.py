#!F:\Other_Py\python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

############

print ("Content-Type: text/html")
print ("")
import cgi,cgitb

##########

list_products=['Alienware 17','Dell 22 Monitor - P2219H','Dell PowerEdge R440 Rack Server']
dataset=pd.read_csv("C:\\Users\\MUJ\\Desktop\\TO\\data2.csv",encoding = "ISO-8859-1")

for i in list_products:
    product=i
    dataset2=dataset.loc[(dataset['Product Type'] ==product)]
    dataset3=dataset2.groupby('service done in warranty period',as_index=False).count()
    dataset3=dataset3[['service done in warranty period','Customer Id']]
    dataset3=dataset3.rename(columns = {'Customer Id':'Pieces Sold'})

    X = dataset3.iloc[:, [0,1]].values

    index = np.arange(len(X[:,0]))
    plt.bar(index, X[:,1])
    plt.xlabel('service done in warranty period')
    plt.ylabel('Units Sold')
    plt.xticks(index, X[:,0])
    plt.title("In Warranty, No. of Service-Wise Distribution of Units Sold of "+product)
    plt.show()

for i in list_products:
    product=i
    dataset2=dataset.loc[(dataset['Product Type'] ==product)]
    dataset3=dataset2.groupby('service done outside warranty period',as_index=False).count()
    dataset3=dataset3[['service done outside warranty period','Customer Id']]
    dataset3=dataset3.rename(columns = {'Customer Id':'Pieces Sold'})

    X = dataset3.iloc[:, [0,1]].values

    index = np.arange(len(X[:,0]))
    plt.bar(index, X[:,1])
    plt.xlabel('service done outside warranty period')
    plt.ylabel('Units Sold')
    plt.xticks(index, X[:,0])
    plt.title("Outside Warranty, No. of Service-Wise Distribution of Units Sold of "+product)
    plt.show()

    
