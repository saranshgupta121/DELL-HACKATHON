#!F:\Other_Py\python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

############

print ("Content-Type: text/html")
print ("")
import cgi,cgitb

##########

list_products=['Alienware 15','Alienware 17','Dell 22 Monitor - P2219H','Dell PowerEdge R440 Rack Server','Dell PowerEdge T30 Server']
#list_regions=['AFR','AMR-N','AMR-S','EMR','EMR-M','EUR','SAR','SEAR','WPR']
dataset=pd.read_csv("C:\\Users\\MUJ\\Desktop\\TO\\data2.csv",encoding = "ISO-8859-1")
#UTF-8 is a multibyte encoding that can represent any Unicode character. ISO 8859-1 is a single-byte encoding that can represent the first 256 Unicode characters. Both encode ASCII exactly the same way.
pred_2018_2019=np.zeros((5,2),dtype=int)## by default creates an array of flaot


row=0
formobject=cgi.FieldStorage()
region =formobject.getvalue('reg')

for product in list_products: #for region in list_regions:
            dataset2=dataset.loc[(dataset['Product Type'] ==product) & (dataset['Location']==region)] ## loc works with column names or labels whereas iloc works with indexes.
            dataset2=dataset2[['Location','Product Type','Year of Purchase']]
            dataset2=dataset2.groupby('Year of Purchase',as_index=False).count()# False to include year of purchase column also
            dataset2=dataset2.rename(columns = {'Location':'Pieces Sold'})
            dataset2=dataset2[['Year of Purchase','Pieces Sold']]
            dataset3=dataset2.loc[dataset2['Year of Purchase']==2018]
            if dataset3.empty:
                pred_2018_2019[row][0]=0 ## col=0 for 2018
            else:
                pred_2018_2019[row][0]=dataset3['Pieces Sold']
                
            X = dataset2.iloc[:, :-1].values# -1 doesnot select last column
            y = dataset2.iloc[:, 1].values# gives row vector for column with number =1
            
               
            regressor = LinearRegression() #first argument is fit_intercept which is by default set to true which means data needs to be centered ie zero mean and unit standard error
            regressor.fit(X, y)
            
            X_test=np.array([[2019]])# to create two 2d array double square brackets to create 2d array
            y_pred = regressor.predict(X_test)
            y_pred=np.asscalar(y_pred)
            y_pred=round(y_pred)
            if(y_pred<0):
                y_pred=0
            pred_2018_2019[row][1]=y_pred ## col= 1 for year 2019
            row+=1
            
            
list_2018_2019=[]
for i in range(2):
    l=[]
    for j in range(5):
        l.append(pred_2018_2019[j][i])
    list_2018_2019.append(l)
    
indexes=np.argsort((list_2018_2019))## returns indexes of elements after sorting in ascending order,indexes remain preserved


final=[]
for i in range(2):
    f=[]
    for j in range(2,5):
        f.append(list_products[indexes[i][j]])
    final.append(f)
final=np.asarray(final)

index = np.arange(len(list_products))
plt.bar(index, pred_2018_2019[:,0])
plt.xlabel('Products')
plt.ylabel('Units Sold')
plt.xticks(index, list_products,fontsize=5)
plt.title("Units Sold of products for the "+region+" year 2018")
plt.show()

index = np.arange(len(list_products))
plt.bar(index, pred_2018_2019[:,1])
plt.xlabel('Products')
plt.ylabel('Units Sold')
plt.xticks(index, list_products,fontsize=5)
plt.title("Units Sold of products for the "+region+" year 2019")
plt.show()

a=str(final[0][0])+'-----'+str(final[1][0])
print (a)
print ('<br> <br>')
a=str(final[0][1])+'-----'+str(final[1][1])
print (a)
print ('<br> <br>')
a=str(final[0][2])+'-----'+str(final[1][2])
print (a)
print ('<br> <br>')


  

  

