#credits to https://www.geeksforgeeks.org/linear-regression-python-implementation/
# for skeleton of code
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics

data_pairs_path = 'data/rbi/crop_data_pairs.csv'
import csv

file = open(data_pairs_path)
csvreader = csv.reader(file)
x_axis_vals = []
y_axis_vals = []

for row in csvreader:

    x_axis_vals.append(row[0:-1])
    y_axis_vals.append(row[-1])
file.close()
X = np.array(x_axis_vals).astype(np.float)
y = np.array(y_axis_vals).astype(np.float)


"""
# load the boston dataset
boston = datasets.load_boston(return_X_y=False)

# defining feature matrix(X) and response vector(y)
X = boston.data
y = boston.target"""

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
													random_state=1)
print(type(X_train))

# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, y_train)

# regression coefficients
print('Coefficients: ', reg.coef_)

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))

# plot for residual error

## setting plot style
plt.style.use('fivethirtyeight')

## plotting residual errors in training data
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train,
			color = "green", s = 10, label = 'Train data')

## plotting residual errors in test data
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test,
			color = "blue", s = 10, label = 'Test data')

## plotting line for zero residual error
plt.hlines(y = 0, xmin = 0, xmax = 3500, linewidth = 2)

## plotting legend
plt.legend(loc = 'upper right')

## plot title
plt.title("Residual errors")

## method call for showing the plot
plt.show()

