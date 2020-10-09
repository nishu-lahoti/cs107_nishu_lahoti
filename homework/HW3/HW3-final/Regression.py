import numpy as np

class Regression():

    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        raise NotImplementedError

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def score(self, X, y):
        raise NotImplementedError