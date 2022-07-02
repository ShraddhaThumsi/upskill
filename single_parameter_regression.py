data_pairs_path = 'data/rbi/crop_data_pairs.csv'
import csv
import numpy as np
from sklearn import datasets, linear_model, metrics
file = open(data_pairs_path)
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
print(type(X_train))

# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, y_train)

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))

# h = b_0 + (b_1 * x_axis_vals)
# epsilon = y_axis_vals - h
# print(epsilon.shape)
# squared_epsilon = epsilon * epsilon
# loss_function = (1/(2*len(x_axis_vals))) * (np.sum(squared_epsilon))
# print(loss_function)