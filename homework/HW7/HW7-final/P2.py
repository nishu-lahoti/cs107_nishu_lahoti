import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

## PROBLEM 2 PART A

# Create the database and set the cursor.
# Drop tables if they already exist.
db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")

# Create model_params table
cursor.execute('''CREATE TABLE model_params (
    id INTEGER,
    desc TEXT,
    param_name TEXT,
    value TEXT)''')

db.commit()

# Create model_coefs table
cursor.execute('''CREATE TABLE model_coefs (
    id INTEGER,
    desc TEXT,
    feature_name TEXT,
    value TEXT)''')

db.commit()

# Create model_results table
cursor.execute('''CREATE TABLE model_results (
    id INTEGER,
    desc TEXT,
    train_score FLOAT,
    test_score FLOAT)''')

db.commit()

# P2B

# Load data from sckitlearn and place into pandas DataFrame
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns = data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 87)

# Write a function to save to database
def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):

    # X_train, X_test, y_train, and y_test should be used to compute test_score and train_score
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    coef, inter = model.coef_, model.intercept_

    # Insert into params table
    for i, j in model.get_params().items():
        cursor.execute('''INSERT INTO model_params (id, desc, param_name, value) VALUES (?, ?, ?, ?)''', (model_id, model_desc, i, j))
    
    # Insert into coefs table
    for i, j in zip(data.feature_names, model.coef_[0]):
        cursor.execute('''INSERT INTO model_coefs (id, desc, feature_name, value) VALUES (?, ?, ?, ?)''', (model_id, model_desc, i, j))

    cursor.execute('''INSERT INTO model_coefs (id, desc, feature_name, value) VALUES (?, ?, ?, ?)''', (model_id, model_desc, "intercept", model.intercept_[0] ))
    
    # Insert into results table
    cursor.execute('''INSERT INTO model_results (id, desc, train_score, test_score) VALUES (?, ?, ?, ?)''', (model_id, model_desc, train_score, test_score))

    db.commit()

# Set the first model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)

# Save the first model to our database
save_to_database(1, 'Baseline model', db, baseline_model, X_train, X_test, y_train, y_test)

# Create the second model, a reduced logistic regression model
feature_cols = ['mean radius', 
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)

# Save the second model to our database
save_to_database(2, 'Reduced model', db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)


# Create the third model, penalized logistic regression model
penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)

# Save the third model to our database
save_to_database(3, 'L1 penalty model', db, penalized_model, X_train, X_test, y_train, y_test)


## DATABASE QUERIES ##

# Print the id of the best model and corresponding test score
cursor.execute("SELECT id, test_score FROM model_results ORDER BY test_score DESC LIMIT 1")
best_results = cursor.fetchall()
print("Best model id:", best_results[0][0], "\nBest validation score:", best_results[0][1])

# Print the feature names and corresponding coefficients of that model
cursor.execute("SELECT feature_name, value FROM model_coefs WHERE id = 3")
coef_results = cursor.fetchall()

for i, j in coef_results:
    print(i, ":", j)

# Use the coefficients extracted from the best model to reproduce the test score of the best performing model

test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
test_model.coef_ = np.array(penalized_model.coef_)
test_model.intercept_ = np.array(penalized_model.intercept_)

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score}')

db.commit()
db.close()