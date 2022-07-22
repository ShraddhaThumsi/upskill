# credits to https://www.geeksforgeeks.org/understanding-logistic-regression/
import numpy as np
import loss_calculator
import matplotlib.pyplot as plt
def plot_regression(X,y,beta):
    x_0 = X[np.where(y==0.0)]
    x_1 = X[np.where(y==1.0)]

    plt.scatter([x_0[:,1]], [x_0[:,2]], c='b', label='y=0')
    plt.scatter([x_1[:,1]], [x_1[:,2]], c='r', label='y=1')

    x1 = np.arange(0,1,0.1)
    x2 = -(beta[0,0] + beta[0,1]*x1)/beta[0,2]
    plt.plot(x1,x2,c='k',label='regression line')

    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend()
    plt.show()

X = loss_calculator.X
y = loss_calculator.y

beta = loss_calculator.beta
numer_iter = loss_calculator.num_of_iters
print('Estimated regression coefficients: ' +  str(beta))
print('No. of iterations' + str(numer_iter))
logistic = loss_calculator.logistic_function(beta, X)
y_pred = loss_calculator.get_predicted_labels(logistic)
print(np.sum(y==y_pred))
plot_regression(X,y,beta)