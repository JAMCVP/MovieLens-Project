#LOAD LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# 1.Data acquisition of the movielens dataset
#IMPORT DATASET

datamovies= pd.read_csv('/home/jamcey/Downloads/Project/Project4_Movielens/movies.csv', sep= '::', names= ['MovieID','Title','Genres'], quotechar= '"', encoding= None, engine= 'python')
#print(datamovies)
datausers= pd.read_csv('/home/jamcey/Downloads/Project/Project4_Movielens/users.csv',sep= '::', encoding= None, engine= 'python')
#print(datausers)
datarating= pd.read_csv('/home/jamcey/Downloads/Project/Project4_Movielens/ratings.csv',sep= '::', encoding= None, engine= 'python')
#print(datarating)

# 2. Perform the Exploratory Data Analysis (EDA) for the users dataset

#Visualize user age distribution

age_group = datausers.groupby('Age').size()
plt.hist(data=age_group,x=datausers.Age, bins=30)
#plt.show()

#Visualize overall rating by users
user_group = datarating.groupby(['Rating']).size()
#print(user_group)
plt.hist(data=user_group,x=datarating.Rating, bins=5)
#plt.show()

# Find and visualize the user rating of the movie Toy Story

data = pd.merge(pd.merge(datarating,datausers),datamovies)
#print(data)
toystory= data[data['Title'] =='Toy Story (1995)']

plt.hist(toystory['Rating'], bins =[1,2,3,4,5],histtype ='bar')
plt.show()
plt.hist(toystory['Age'],bins = [1,18,25,35,45,50,56],histtype= 'bar')
#plt.show()
#Find and visualize the viewership of the movie Toy Story by age group

