#credits to https://www.geeksforgeeks.org/linear-regression-python-implementation/
# for skeleton of code
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import os
import csv
dirname = os.path.dirname(__file__)

relative_path_to_file = '../data/preprocessed_files/rbi/crop_data_pairs.csv'
filename = os.path.join(dirname, relative_path_to_file)
file = open(filename)
csvreader = csv.reader(file)
x_axis_vals = []
y_axis_vals = []

for row in csvreader:

    x_axis_vals.append(row[0:-1])
    y_axis_vals.append(row[-1])
file.close()
X = np.array(x_axis_vals).astype(np.float)
y = np.array(y_axis_vals).astype(np.float)


# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
													random_state=1)


# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, y_train)

# regression coefficients
print('Coefficients: ', reg.coef_)

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))

print("printing shape of train data - data first, label 2nd")
print(X_train.shape)
print(y_train.shape)


print("printing shape of test data -data first, label 2nd")
print(X_test.shape)
print(y_test.shape)
# plot for residual error
def plot_variance():
	## setting plot style
	plt.style.use('fivethirtyeight')

	## plotting residual errors in training data
	plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train,
				color="green", s=10, label='Train data')

	## plotting residual errors in test data
	plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test,
				color="blue", s=10, label='Test data')

	## plotting line for zero residual error
	# plt.hlines(y=reg.score(X_train, y_train),xmin=0,xmax=3500,linewidth=2,color='b',label='closeness score of train data')
	plt.hlines(y=reg.score(X_test, y_test), xmin=0, xmax=3500, linewidth=2, color='r',
			   label='closeness score of test data')

	## plotting legend
	plt.legend(loc='lower right')

	## plot title
	plt.title("Closeness to true total cereal production in lakh tonnes from 1950-2021")

	## method call for showing the plot
	plt.show()
plot_variance()

