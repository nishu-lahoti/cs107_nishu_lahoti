from sklearn import datasets
import numpy as np

class Regression():

    # Initializing the class with empty parameters dictionary.
    def __init__(self):
        self.params = {}
    
    # Simple argument to return the dictionary values
    def get_params(self):
        return self.params

    # Useful for setting multiple parameters in the Ridge Regression
    def set_params(self, **kwargs):
        for k, v in kwargs.items():
            self.params[k] = v
        raise NotImplementedError

    # Method that applies the called fit formula from subclass.
    def fit(self, X, y):
        raise NotImplementedError

    # Uses the parameters to complete prediction.
    def predict(self, X):
        raise NotImplementedError

    # Computes the R2 score
    def score(self, X, y):
        raise NotImplementedError

class LinearRegression(Regression):
    
    # Starts by determining the rows and column lengths of X
    # and appends a column of ones to help compute intercepts.
    # Then compute the coefficient formula from the inside out
    # starting with determining x_tranpose, the inverse of a matrix
    # multiplication, and the matrix multiplication of x_tranpose and y.
    # Puts this all together into a beta value which is passed into self.params
    # dictionary.

    def __init__(self):
        super(LinearRegression, self).__init__()

    def fit(self, X, y):
        (n, p) = X.shape
        x_new = np.append(X, np.ones((n, 1)), axis = 1)

        x_transpose = np.transpose(x_new)
        x_inv = np.linalg.pinv(np.matmul(x_transpose, x_new))
        y_value = np.matmul(x_transpose, y)
        self.beta = np.matmul(x_inv, y_value)
        # self.beta = inv(np.matmul(np.transpose(x_new), x_new)) * (np.transpose * y)
        self.params = {'intercept': self.beta[-1], 'coefficients': self.beta[:-1]}


    # Takes the values from fit method and places them in the y = X*B formula to 
    # determine the linear regression.

    def predict(self, X):
        ols =  np.dot(X, self.params['coefficients']) + self.params['intercept']
        return ols

    # Applies the formulas in the prompt to determine the R2 score.
    def score(self, X, y):
        y_mean = np.mean(y)
        y_predicted = self.predict(X)
        sst = np.sum((y - y_mean)**2)
        sse = np.sum((y - y_predicted)**2)
        R2 = 1 - (sse / sst)
        return R2


class RidgeRegression(LinearRegression):
    
    # Initializes the class with the alpha parameter.
    def __init__(self, alpha):
        super(RidgeRegression, self).__init__()
        self.params['alpha'] = alpha

    # Similar to the strategy from above, computes the beta coefficients from the inside
    # out. Starting with gathering the shape of X and utilizing that to set an add'l column
    # of intercepts before using transposed and inversed values to do matrix multiplication.
    # Finally, computs beta coefficients and places them in self.params dictionary.
    def fit(self, X, y):
        (n, p) = X.shape

        x_new = np.append(X, np.ones((n, 1)), axis = 1)
        reg = np.dot(self.params['alpha'], np.identity(p+1))
        x_transpose = np.transpose(x_new)
        inner = x_transpose.dot(x_new) + reg
        inner_inv = np.linalg.inv(inner)
        # inner = reg + np.linalg.inv(np.matmul(x_transpose, x_new))
        outer = np.matmul(x_transpose, y)
        self.beta = np.matmul(inner_inv, outer)
        # self.beta = (inv(np.transpose(x_new) * x_new) + (inv(self.alpha) * self.alpha)) * (np.transpose * y)
        self.params = {'intercept': self.beta[-1], 'coefficients': self.beta[:-1]}

    # Similarly uses the y = X*B equation to compute predicted values.
    def predict(self, X):
        ridge = np.dot(X,self.params['coefficients']) + self.params['intercept']
        print(self.get_params()['intercept'])
        return ridge

    # Applies the formulas in the prompt to determine the R2 score.
    def score(self, X, y):
        y_mean = np.mean(y)
        y_predicted = self.predict(X)
        sst = np.sum((y - y_mean)**2)
        sse = np.sum((y - y_predicted)**2)
        R2 = 1 - (sse / sst)
        return R2