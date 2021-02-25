import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

data=pd.read_csv(r'C:\Users\Pradeepa\Desktop\udemy dataset\New folder\Regression\Section 6 - Simple Linear Regression\Python/salary.csv')

null=data.isnull().any()

X=data[['YearsExperience']].values.reshape(-1,1)
y=data.iloc[:,1].values
print(data.head())


from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)



pickle.dump(model,open('salary.pkl','wb'))