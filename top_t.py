#!F:\Other_Py\python

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

############

print ("Content-Type: text/html")
print ("")
import cgi,cgitb

##########


list_products=['Alienware 15','Alienware 17','Dell 22 Monitor - P2219H','Dell PowerEdge R440 Rack Server','Dell PowerEdge T30 Server']
list_regions=['AFR','AMR-N','AMR-S','EMR','EMR-M','EUR','SAR','SEAR','WPR']
dataset=pd.read_csv("C:\\Users\\MUJ\\Desktop\\TO\\data2.csv",encoding = "ISO-8859-1")

product_2018_2019=np.zeros((5,9),dtype=int)

row=0
#region='WPR' ## given by user
#for product in list_products: #for region in list_regions:
#product='Alienware 17'
col=0
for product in list_products:
    col=0
    for region in list_regions:
        dataset2=dataset.loc[(dataset['Product Type'] ==product) & (dataset['Location']==region)] ## loc works with column names or labels whereas iloc works with indexes.
        dataset2=dataset2[['Location','Product Type','Year of Purchase','price in dollars']]
        # False to include year of purchase column also
        dataset2.drop_duplicates(subset ='price in dollars',keep = 'first', inplace = True) 
       
            
        X = dataset2.iloc[:,[2]].values# -1 doesnot select last column
        y = dataset2.iloc[:,3].values# gives row vector for column with number =1
    
       
        regressor = LinearRegression() #first argument is fit_intercept which is by default set to true which means data needs to be centered ie zero mean and unit standard error
        regressor.fit(X, y)
        
        X_test=np.array([[2019]])# to create two 2d array double square brackets to create 2d array
        y_pred = regressor.predict(X_test)
        y_pred=np.asscalar(y_pred)
        y_pred=round(y_pred)
        product_2018_2019[row][col]=y_pred ## col= 1 for year 2019
        col+=1
    row+=1
ans=[]
s=0
for i in range (0,9):
    s=0
    for j in range (0,5):
        s=s+product_2018_2019[j][i]
    ans.append(3*s)


index = np.arange(len(list_regions))
plt.bar(index, ans)
plt.xlabel('Regions')
plt.ylabel('Predicted Revenue')
plt.xticks(index, list_regions,fontsize=5)
plt.title("Revenue for the year 2019")
plt.show()

print ("Africa Region" , "------>" , ans[0])
print ('<br>')
print ('<br>')
print ("North America Region" , "------>" , ans[1])
print ('<br>')
print ('<br>')
print ("South America Region" , "------>" , ans[2])
print ('<br>')
print ('<br>')
print ("Eastern M.R." , "------>" , ans[3])
print ('<br>')
print ('<br>')
print ("Middle Eastern M.R." , "------>" , ans[4])
print ('<br>')
print ('<br>')
print ("Europe Region" , "------>" , ans[5])
print ('<br>')
print ('<br>')
print ("South Asia Region" , "------>" , ans[6])
print ('<br>')
print ('<br>')
print ("South East Asia Region" , "------>" , ans[7])
print ('<br>')
print ('<br>')
print ("Western Pacific Region" , "------>" , ans[8])



