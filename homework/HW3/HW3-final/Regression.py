from sklearn import datasets
import numpy as np

class Regression():

    def __init__(self):
        self.params = {}

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        for k, v in kwargs.items():
            self.params[k] = v
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

        x_transpose = np.transpose(x_new)
        x_inv = np.linalg.pinv(np.matmul(x_transpose, x_new))
        y_value = np.matmul(x_transpose, y)
        self.beta = np.matmul(x_inv, y_value)
        # self.beta = inv(np.matmul(np.transpose(x_new), x_new)) * (np.transpose * y)
        self.params = {'intercept': self.beta[-1], 'coefficients': self.beta[:-1]}

    def predict(self, X):
        ols =  X * self.params['coefficients'] + self.params['intercept']
        return ols

    # def score(self, X, y):


class RidgeRegression(LinearRegression):
    
    def __init__(self, alpha):
        super(LinearRegression).__init__()
        self.alpha = alpha

    def fit(self, X, y):
        (n, p) = X.shape
        reg = np.matmul(self.alpha, np.identity(p))
        x_new = np.append(X, np.ones((n, 1)), axis = 1)
        x_transpose = np.transpose(x_new)
        inner = np.linalg.inv(np.matmul(x_transpose, x_new) + reg)
        outer = np.matmul(x_transpose, y)
        self.beta = np.matmul(inner, outer)
        # self.beta = (inv(np.transpose(x_new) * x_new) + (inv(self.alpha) * self.alpha)) * (np.transpose * y)
        self.params = {'intercept': self.beta[-1], 'coefficients': self.beta[:-1]}

    def predict(self, X):
        ridge = X * self.params['coefficients'] + self.params['intercept']
        return ridge

    # def score(self, X, y):

### Test ###

# dataset = datasets.load_boston(return_X_y = TRUE)
# first = sklearn()
# first.fit(X,y)

# second = LinearRegression()
# second.fit(X, y)

# print("Intercept: ", first.intercept_)
# print("Coefficients: ", first.coef_)

# print("Intercept: ", second.get_params()['intercept']
# print("Coefficients: ", second.get_params()['coefficients'])