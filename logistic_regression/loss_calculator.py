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
normalized_data = normalize(X)

def logistic_function(beta,X):
    return 1.0/(1+np.exp(np.dot(beta.T,X)))

