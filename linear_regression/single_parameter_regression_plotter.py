from linear_regression import single_parameter_regression

print('b_0')
print(single_parameter_regression.b_0)
print('b_1')
print(single_parameter_regression.b_1)
import matplotlib.pyplot as plt

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
b_0 = single_parameter_regression.b_0
b_1 = single_parameter_regression.b_1
x = single_parameter_regression.x_axis_vals
y = single_parameter_regression.y_axis_vals
plot_regression_line(x, y, b_0,b_1)