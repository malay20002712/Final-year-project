# -*- coding: utf-8 -*-
"""temperaturePrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GzWUgSl81zl1jb6dvuL_4yp6aAyC2BfD
"""

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb

from google.colab import files
uploaded = files.upload()

temperature_data = pd.read_csv ('/content/temp.csv')

temperature_data

temperature_data.columns

figure = plt.figure(figsize = (10, 10))
sb.heatmap(temperature_data.isna(),cbar=False)
plt.show()
print((temperature_data.isna().sum()/temperature_data.shape[0]*100).sort_values(ascending=False))

plt.figure(figsize=(20, 8), dpi=100)
plt.plot(temperature_data["Next_Tmax"],label="Highest Temperature")
plt.plot(temperature_data["Next_Tmin"],label="Lowest Temperature")
plt.legend()
plt.show()

print ("Next_Tmax : HIGHEST TEMPERATURE")
print ("Next_Tmin: LOWEST TEMPERATURE")
for col in ["Next_Tmax","Next_Tmin"]:
    plt.figure()
    sb.displot(temperature_data[col],kind='kde')
    plt.show()
print(temperature_data["Next_Tmax"].mean())
print(temperature_data["Next_Tmax"].std())
print(temperature_data["Next_Tmin"].mean())
print(temperature_data["Next_Tmin"].std())

plt.figure(figsize = (6, 5))
plt.xlabel("highest Temperature")
plt.ylabel ("Lowest Temperature")
sb.heatmap(pd.crosstab(temperature_data['Next_Tmax'],temperature_data['Next_Tmin']))
plt.show()

"""Now we preprocess the data"""

temperature_preprocess = pd.read_csv("/content/temp.csv")

def remove_var(temperature):
  temperature.drop(["Date"], axis = 1, inplace = True)
  # as we donot need the date variable in this thats why we drop date variable
  print (temperature_data.dtypes.value_counts())
  return temperature

"""Now remove the null values from all the rows"""

def cleaning_data (temperature):
  temperature.dropna(axis = 0, inplace = True)
  return temperature

def endcode(temperature):
  return temperature

#the work of the function inside this cell will be just to preprocess the data after certainly cleaning it
def preprocess_temperature_data(temperature_data):
  # now first we call the function to clean the data
  temperature_data = cleaning_data(temperature_data)
  temperature_data = endcode(temperature_data)
  temperature_data = remove_var(temperature_data)

  remove = ['Next_Tmax', 'NextTmin']
  X = temperature_data[temperature_data.columns.difference(remove)]
  ymax = temperature_data['Next_Tmax']
  ymin = temperature_data['Next_Tmin']
  print (X.shape)
  print (ymax.shape)
  print (ymin.shape)
  return X, ymax, ymin

!pip install sklearn

from sklearn.model_selection import train_test_split

trainset,testset = train_test_split(temperature_data, test_size = 0.2, random_state = 0)

X_train, y_max_train, y_min_train = preprocess_temperature_data(trainset)
X_test, y_max_test, y_min_test = preprocess_temperature_data(testset)

"""Making the model

Applying Random Forest Search
"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

param_grid = {
    'bootstrap': [True],
    'max_depth': [70, 130],
    'max_features': [3, 6],
    'min_samples_leaf': [2, 3],
    'min_samples_split': [4, 8],
    'n_estimators': [1000, 500]
}
rf = RandomForestRegressor()
grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, 
                          cv = 3, n_jobs = -1, verbose = 2)

def evaluate(model, test_features, test_labels):
    predictions = model.predict(test_features)
    errors = abs(predictions - test_labels)
    mape = 100 * np.mean(errors / test_labels)
    accuracy = 100 - mape
    print('Average Error: {:0.4f} degrees.'.format(np.mean(errors)))
    print('Accuracy = {:0.2f}%.'.format(accuracy))
    print (predictions)
    
    return predictions

grid_search.fit(X_train, y_max_train)
print(grid_search.best_params_)
best_grid = grid_search.best_estimator_
grid_accuracy = evaluate(best_grid, X_test, y_max_test)

base_model = RandomForestRegressor(n_estimators = 10, random_state = 42)
base_model.fit(X_train, y_max_train)
base_accuracy = evaluate(base_model, X_test, y_max_test)

# print('Improvement of {:0.2f}%.'.format( 100 * (grid_accuracy - base_accuracy) / base_accuracy))
import statistics as st
e = st.mean(base_accuracy)
if e < 50:
  print("Weather is fantastic")
else:
  print('Its gonna be rain you should not go out')



