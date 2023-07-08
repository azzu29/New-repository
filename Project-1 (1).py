#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem Statement –

 #You are the Data Scientist at a telecom company “Neo” whose customers are churning out to its competitors. 
    #You have to analyze the data of your company and find insights and stop your customers from churning out
    #to other telecom companies.


# In[21]:


#Starts here...

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

info = pd.read_csv("customer_churn 1.csv")
info


# In[11]:


info = info.rename(columns = {'gender : 1': 'Gender'})
info


# In[34]:


info.info()


# In[35]:


# info.iloc[:,:]

info.iloc[0:10]


# In[ ]:





# In[ ]:


# A) Data Manipulation:....


# In[213]:


#ANSWER-1

customer_5 = info.loc[:6,"tenure"]
customer_5


# In[155]:


#ANSWER-2

customer_15 = info.loc[:5, "PaperlessBilling"]
customer_15


# In[75]:


info.head(10)


# In[ ]:





# In[ ]:





# In[13]:


#ANSWER-3

#In this we are extracting the male citizen with the electronic payment method...with the help 
#of filter method and storing it in the senior_male_electronic....

senior_male_electronic = info[(info['gender'] == 'Male') & (info['SeniorCitizen'] == 1) & 
                          (info['PaymentMethod'] == 'Electronic check')]

senior_male_electronic


# In[ ]:





# In[80]:


#ANSWER-4

#We are extracting the tenure col more than 70 and mobilecharges more than 100, we use filter method and then 
#store it in the customer_total_tenure.

customer_tenure = (info['tenure']> 70) & (info['MonthlyCharges'] > 100)

customer_total_tenure = info[customer_tenure] 
customer_total_tenure


# In[ ]:





# In[129]:


#ANSWER-5
    
#Collect the information from contract of 2yrs, payment method of mailed check and churn of yes....

two_mail_yes = info[(info['Contract'] == 'Two year') & (info['PaymentMethod'] == 'Mailed check') & (info['Churn'] == 'Yes')]
two_mail_yes


# In[ ]:





# In[156]:


#ANSWER-6
    
#Here we can get the individual data by iloc....    
    
customer_333 = info.iloc[333]
customer_333


# In[ ]:





# In[150]:


#ANSWER-7
    
# info

feature = "Churn"
info[feature].value_counts() #This is used For the counts in the particular columns 

# info[feature].unique()  #This is used for showing the objects in a particular columns


# In[ ]:





# In[157]:


# B) Data Visualization:....


# In[159]:


info


# In[207]:


# info.select_dtypes(include = ['object'])

feature = 'InternetService'
info[feature].value_counts()


# In[16]:


#a. Build a bar-plot for the ’InternetService’ column:

import numpy as np
import matplotlib.pyplot as plt

data = {'No' : 1526, 'DSL' : 2421, 'Fiber optic' : 3096}
names = list(data.keys())
values = list(data.values())

# fig = plt.figure(figsize=(10,5))

plt.bar(names,values, color='orange')
plt.title("Distribution of Internet Services")
plt.show()


# In[ ]:





# In[ ]:


#b. Build a histogram for the ‘tenure’ column:


# In[215]:


bins = info.loc[:30, "tenure"]
bins


# In[ ]:





# In[63]:


import matplotlib.pyplot as plt
import numpy as np

#Generate the data of tenure
# data = np.tenure.random.randint(low=1, high=50, size=500)

tenure_data = [1, 34, 2, 45, 2, 8, 22, 10, 28, 62, 13, 16, 58, 49, 25, 69, 52, 71, 10, 21, 1, 12, 1, 58, 49, 30, 47, 1, 72, 17, 71]

#Setting the number of bins and color
plt.hist(tenure_data, bins=30, color='green')

#Adding title...
plt.title('Distribution of tenure')
plt.show()


# In[195]:


info


# In[ ]:





# In[ ]:


# c. Build a scatter-plot between ‘MonthlyCharges’ & ‘tenure’. Map ‘MonthlyCharges’ to the y-axis & 
# ‘tenure’ to the ‘x-axis’:


# In[83]:



import matplotlib.pyplot as plt
import pandas as pd 

#extracting the file..
data = pd.read_csv("customer_churn 1.csv")

#extracting the monthlycharges and tenure columns..
monthly_charges = data["MonthlyCharges"]
tenuree = data["tenure"]

plt.scatter(tenuree, monthly_charges, color='brown')

#labels, titles and print...
plt.xlabel("Tenure of Customers")
plt.ylabel("Monthly Charges of Customers")
plt.title("Tenure Vs Monthly Charges")
plt.show()


# In[ ]:





# In[ ]:


# d. Build a box-plot between ‘tenure’ & ‘Contract’. Map ‘tenure’ on the y-axis & ‘Contract’ on the x-axis.


# In[ ]:





# In[81]:


import matplotlib.pyplot as plt
import pandas as pd

#extracting the file
data = pd.read_csv("customer_churn 1.csv")

#creating the boxplot...We group the box plots by contract using the by parameter..and column is also used for grouping the plots..
data.boxplot(column = "tenure", by = "Contract")

#labels and titles
plt.ylabel("Tenure")
plt.xlabel("Contract")
# plt.title("Box-ploting of Tenure and Contract")
plt.show()


# In[ ]:





# In[ ]:


......................THE END..........................


# In[ ]:




