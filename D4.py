#Task4:Pandas basic
#Data wrangling, also known as data munging, is the process of transforming raw data into a usable and structured format for analysis or machine learning
import pandas as pd

#sample data dictionary
data={
    'Name':['Nayan','Divya','Kartik','Loki'],
    'Age':[21,22,21,21],
    'Score':[90.2,88.0,95.6,85.5]
}

#Creating dataframe
df= pd.DataFrame(data)

#print dataframe
print(df)

#Basic info about data
print("\nShape of data:",df.shape)
print("\nColumns:",df.columns.tolist())
print("\nData types:\n",df.dtypes)

#summary stats
print("\nSummary stats:\n",df.describe())

#Access column
print("\nAges:",df['Age'].tolist())

#Filter rows
print("\nPeople with age>21:\n",df[df['Age']>21])

#Calculate mean
print("\nAverage Score:",df['Score'].mean())