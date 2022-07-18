import numpy as np
import loss_calculator
import matplotlib as plt
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
beta = np.matrix(np.zeros(X.shape[1]))
beta, numer_iter = loss_calculator.gradient_descent(X,y,beta)
print('Estimated regression coefficients: ' +  beta)
print('No. of iterations' + numer_iter)
y_pred = loss_calculator.pred_values(beta,X)
print(np.sum(y==y_pred))
plot_regression(X,y,beta)