#!F:\Other_Py\python

import pandas as pd
import numpy as np, json, math
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

############

print ("Content-Type: text/html")
print ("")
import cgi,cgitb

##########


list_regions=['AFR','AMR-N','AMR-S','EMR','EMR-M','EUR','SAR','SEAR','WPR']
dataset=pd.read_csv("C:\\Users\\MUJ\\Desktop\\TO\\data2.csv",encoding = "ISO-8859-1")

formobject=cgi.FieldStorage()
product =formobject.getvalue('pro')
#'Alienware 17'
    
product_2018_2019=np.zeros((2,9))
col=0
for region in list_regions:
    dataset2=dataset.loc[(dataset['Product Type'] ==product) & (dataset['Location']==region)]
    dataset2=dataset2[['Location','Product Type','Year of Purchase']]
    dataset3=dataset2.groupby('Year of Purchase',as_index=False).count()
    dataset3=dataset3.rename(columns = {'Location':'Pieces Sold'})
    dataset3=dataset3[['Year of Purchase','Pieces Sold']]
    dataset4=dataset3.loc[dataset3['Year of Purchase']==2018]
    dataset4=dataset4[['Pieces Sold']]
    if dataset4.empty:
        product_2018_2019[0][col]=0
    else:
        product_2018_2019[0][col]=dataset4['Pieces Sold']
    
    X = dataset3.iloc[:, :-1].values
    y = dataset3.iloc[:, 1].values
    
       
    regressor = LinearRegression()
    regressor.fit(X, y)
    
    X_test=np.array([[2019]])# to create two 2d array
    y_pred = regressor.predict(X_test)
    y_pred=round(np.asscalar(y_pred))
    product_2018_2019[1][col]=y_pred
    col+=1


ans=[]

ans.append(product_2018_2019[0][0]); ans.append(product_2018_2019[1][0]); ans.append(product_2018_2019[0][1]);
ans.append(product_2018_2019[1][1]); ans.append(product_2018_2019[0][2]); ans.append(product_2018_2019[1][2]);
ans.append(product_2018_2019[0][3]); ans.append(product_2018_2019[1][3]); ans.append(product_2018_2019[0][4]);
ans.append(product_2018_2019[1][4]); ans.append(product_2018_2019[0][5]); ans.append(product_2018_2019[1][5]);
ans.append(product_2018_2019[0][6]); ans.append(product_2018_2019[1][6]); ans.append(product_2018_2019[0][7]);
ans.append(product_2018_2019[1][7]); ans.append(product_2018_2019[0][8]); ans.append(product_2018_2019[1][8]);

#Ans={
#  "l1": math.floor(ans[0]) , "l2": math.floor(ans[1]), "l3": math.floor(ans[2]), "l4": math.floor(ans[3]), "l5": math.floor(ans[4]), "l6": math.floor(ans[5]),
#  "l7": math.floor(ans[6]), "l8": math.floor(ans[7]), "l9": math.floor(ans[8]), "l10": math.floor(ans[9]), "l11": math.floor(ans[10]), "l12": math.floor(ans[11]),
#  "l13": math.floor(ans[12]), "l14": math.floor(ans[13]), "l15": math.floor(ans[14]), "l16": math.floor(ans[15]), "l17": math.floor(ans[16]), "l8": math.floor(ans[17]), 
#}
#fAns=json.dumps(Ans)
#print(fAns)


a=str(math.floor(ans[0]))+'---------->'+str(math.floor(ans[1]))
print (a)
print ('<br> <br>')
a=str(math.floor(ans[2]))+'---------->'+str(math.floor(ans[3]))
print (a)
print ('<br> <br>')
a=str(math.floor(ans[4]))+'---------->'+str(math.floor(ans[5]))
print (a)
print ('<br> <br>')
a=str(math.floor(ans[6]))+'---------->'+str(math.floor(ans[7]))
print (a)
print ('<br> <br>')
a=str(math.floor(ans[8]))+'---------->'+str(math.floor(ans[9]))
print (a)
print ('<br> <br>')
a=str(math.floor(ans[10]))+'---------->'+str(math.floor(ans[11]))
print (a)
print ('<br> <br>')
a=str(math.floor(ans[12]))+'---------->'+str(math.floor(ans[13]))
print (a)
print ('<br> <br>')
a=str(math.floor(ans[14]))+'---------->'+str(math.floor(ans[15]))
print (a)
print ('<br> <br>')
a=str(math.floor(ans[16]))+'---------->'+str(math.floor(ans[17]))
print (a)
print ('<br> <br>')


plt.pie(product_2018_2019[0,:], labels=list_regions, startangle=90, autopct='%.1f%%')
plt.title("Sales Distribution for "+product+" for year 2018")
plt.show()


plt.pie(product_2018_2019[1,:], labels=list_regions, startangle=90, autopct='%.1f%%')
plt.title("Sales Distribution for "+product+" for year 2019")
plt.show()






