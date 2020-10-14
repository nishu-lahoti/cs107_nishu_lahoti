from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import LinearRegression, RidgeRegression

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)


lr = LinearRegression()
lr.fit(X_train, y_train)

print("Intercept: ", lr.get_params()['intercept'])
print("Coefficients: ", lr.get_params()['coefficients'])


alpha = 0.5
ridge = RidgeRegression(alpha)
print("Intercept: ", ridge.get_params()['intercept'])
print("Coefficients: ", ridge.get_params()['coefficients'])

# models = [LinearRegression(), RidgeRegression(alpha)]

# for model in models:
#     model.fit(X_train, y_train);

    