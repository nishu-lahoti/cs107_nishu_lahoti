import numpy as np
import np.linalg.pinv as inv

class Regression():

    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        raise NotImplementedError

    def fit(self, X, y):
        # self.params = {X : y}
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def score(self, X, y):
        raise NotImplementedError

class LinearRegression(Regression):
    
    def fit(self, X, y):
        (n, p) = X.shape
        x_new = np.append(X, np.ones((n, 1)), axis = 1)
        beta = inv(np.transpose(x_new) * x_new) * (np.transpose * y)
        self.params = {'intercept': beta[-1], 'coefficients': beta[:-1]}

    def predict(self, X):
        ols =  X * self.params['coefficients'] + self.params['intercept']
        return ols


class RidgeRegression(LinearRegression):
    