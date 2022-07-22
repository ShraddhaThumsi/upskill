

import csv
import numpy as np
from sklearn import linear_model
import os
import matplotlib.pyplot as plt
dirname = os.path.dirname(__file__)
data_pairs_path = '../data/preprocessed_files/rbi/crop_data_pairs.csv'
filename = os.path.join(dirname, data_pairs_path)
file = open(filename)
csvreader = csv.reader(file)

x_axis_vals = []
y_axis_vals = []
y_axis_vals_2 = []
rows = []
for row in csvreader:
    rows.append(row)
    x_axis_vals.append(row[0])
    y_axis_vals.append(row[1])
    y_axis_vals_2.append(row[2])

file.close()
x_axis_vals = np.array(x_axis_vals).astype(np.float)
y_axis_vals = np.array(y_axis_vals).astype(np.float)
y_axis_vals_2 = np.array(y_axis_vals).astype(np.float)

def find_deviations(axis_1, axis_2):
    n = len(axis_1)

    axis_1 = np.array(axis_1).astype(np.float)
    axis_2 = np.array(axis_2).astype(np.float)
    mean_1 = np.mean(axis_1)


    mean_2 = np.mean(axis_2)

    running_sum = 0
    for i in range(0,n):
        v1 = axis_1[i]
        v2 = axis_2[i]

        running_sum += (v1*v2)

    return running_sum - (n * mean_1 * mean_2)

deviation_xx = find_deviations(axis_1=x_axis_vals, axis_2=x_axis_vals)
deviation_xy = find_deviations(axis_1= x_axis_vals, axis_2 = y_axis_vals_2)

b_1 = deviation_xy/deviation_xx
b_0 = np.mean(y_axis_vals_2) - (b_1 * np.mean(x_axis_vals))


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_axis_vals.reshape(-1,1), y_axis_vals, test_size=0.4,
													random_state=1)


# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, y_train)

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))

print("printing shape of train data - data first, label 2nd")
print(type(X_train))
print(X_train.shape)
print(type(y_train))
print(y_train.shape)


print("printing shape of test data -data first, label 2nd")
print(type(X_test))
print(X_test.shape)
print(type(y_test))
print(y_test.shape)

def plot_predictions_and_scores():
    ## setting plot style
    plt.style.use('fivethirtyeight')
    plt.ylim(-1,1)

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

def plot_regression_line(x, y, b_0,b_1):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b_0 + b_1 * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()
print("values of predictions on training data")
for i in list(reg.predict(X_train)):
    print(i)


print("value of predictions of testing data")
for i in list(reg.predict(X_test)):
    print(i)
plot_predictions_and_scores()

#plot_regression_line(x_axis_vals, y_axis_vals, b_0,b_1)