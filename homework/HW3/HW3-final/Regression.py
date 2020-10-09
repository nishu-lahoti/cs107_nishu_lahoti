import numpy as np

class Regression():

    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        for key, value in kwargs.items():
            print ("%s == %s" %(key, value))
        raise NotImplementedError

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def score(self, X, y):
        raise NotImplementedError

# Test
args = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}

d1 = Regression()
d1.get_params()
d1.set_params(**args)
d1.fit()
d1.predict()
d1.score()