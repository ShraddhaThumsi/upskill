# credits to https://www.geeksforgeeks.org/understanding-logistic-regression/ for blueprint
import numpy as np
import data_loader_and_preprocessor
X = data_loader_and_preprocessor.X
y = data_loader_and_preprocessor.y


def normalize(data):
    #the data is not in the same range, so we will normalize it to avoid influence of one feature over another
    minval = np.min(data)
    maxval = np.max(data)
    range_of_data = maxval - minval
    normalized = 1- ((maxval-data)/range_of_data)
    return normalized
X = normalize(X)

def logistic_function(beta,X):
    return 1.0/(1+np.exp(np.dot(X,beta.T)))

def gradient_of_sigmoid_wrt_params(beta, X, y):
    predicted_value = logistic_function(beta,X)
    diff_in_preds = predicted_value - y
    gradient = np.dot(diff_in_preds.T,X)
    return gradient



beta = np.matrix(np.zeros(X.shape[1]))
logistic = logistic_function(beta,X)
gradient = gradient_of_sigmoid_wrt_params(beta, X, y)
print(logistic)
print(gradient)

