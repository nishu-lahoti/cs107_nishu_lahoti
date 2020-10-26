from Regression import LinearRegression, RidgeRegression
from sklearn import datasets
import matplotlib as mp

# Imported data to be used for performance testing
X, y = datasets.load_boston(return_X_y = True)

# Attempted to create a list of alpha values to pass into ridge performance
alphas = [0.01, 0.1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Setting variables with Ridge and Linear Regression Classes
ridge_performance = RidgeRegression.set_params(alphas)
linear_performance = LinearRegression()

# Fitting the models to each type of regression
ridge_performance.fit(X, y)
linear_performance.fit(X, y)

# Here is where I would implement matplotlib to visualize