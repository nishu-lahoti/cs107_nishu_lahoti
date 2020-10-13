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
        X = np.array(X).reshape(-1, 1)
        y = np.array(y).reshape(-1, 1)
        self.params = {X, y}

    def predict(self, X):
        self.coef = {np.inv(np.transpose(X) * X) * (np.transpose * self.get_params(X)), self.get_params(X)}