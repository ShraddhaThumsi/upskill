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

def cost_function(beta,X,y):
    predicted_val = logistic_function(beta,X)
    loss_value_array = - (y * np.log(predicted_val)) - ((1-y)*np.log(1-predicted_val))
    return np.mean(loss_value_array)

def gradient_descent(beta,X,y, learning_rate = 0.01, convergence_threshold = 0.0001):
    total_cost = cost_function(beta,X,y)
    change_of_cost = 1
    num_of_iter = 1
    while(change_of_cost > convergence_threshold):
        old_cost = total_cost
        beta = beta - (learning_rate * gradient_of_sigmoid_wrt_params(beta,X,y))
        total_cost = cost_function(beta,X,y)
        change_of_cost = old_cost - total_cost
        num_of_iter += 1
    return beta, num_of_iter
beta = np.matrix(np.zeros(X.shape[1]))
print("shape of beta")
print(beta.shape)
logistic = logistic_function(beta,X)
gradient = gradient_of_sigmoid_wrt_params(beta, X, y)
total_cost = cost_function(beta,X,y)
beta, num_of_iters = gradient_descent(beta,X,y)
print("shape of activation function")
print(logistic.shape)
print("shape of logistic gradient")
print(gradient.shape)
print("shape of total cost")
print(total_cost)
print("shape of predicted beta ")
print(beta.shape)
print(num_of_iters)

def get_predicted_labels(logistic):
    probabilities = logistic
    print("shape of probabilities")
    print(probabilities.shape)
    predicted_labels = np.where(probabilities >= 0.5,1,0)
    return np.squeeze(predicted_labels)

predicted_labels = get_predicted_labels(logistic)
print("shape of estimated parameter array beta:")
print(beta.shape)
"""print("shape of true labels")
print(y.shape)
print("shape of predicted labels")
print(predicted_labels.shape)
print("totally correct predictions:")
print(np.sum(y==predicted_labels))"""



