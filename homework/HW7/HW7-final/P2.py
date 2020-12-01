import sqlite3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

# P2A

db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")

# Create model_params table
cursor.execute('''CREATE TABLE model_params (
    id INTEGER PRIMARY KEY NOT NULL,
    desc TEXT,
    param_name TEXT,
    value INTEGER)''')

db.commit()

# Create model_coefs table
cursor.execute('''CREATE TABLE model_coefs (
    id INTEGER PRIMARY KEY NOT NULL,
    desc TEXT,
    feature_name TEXT,
    value INTEGER)''')

db.commit()

# Create model_results table
cursor.execute('''CREATE TABLE model_results (
    id INTEGER PRIMARY KEY NOT NULL,
    desc TEXT,
    train_score INTEGER,
    test_score INTEGER)''')

db.commit()

# P2B

# Load data
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
    param_keys = model.get_params().keys() 
    param_values = model.get_params().values() # How to convert these values to string
    param_values = str(model.get_params().values())
    coef, inter = model.coef_, model.intercept_

    vals_to_insert_param = (model_id, model_desc, param_keys, param_values)
    vals_to_insert_coef = (model_id, model_desc, coef, inter)
    vals_to_insert_results = (model_id, model_desc, train_score, test_score)

    # Insert the model information to the corresponding tables
    cursor.execute('''INSERT INTO model_params (id, desc, param_name, value) VALUES (?, ?, ?, ?)''', vals_to_insert_param)
    cursor.execute('''INSERT INTO model_params (id, desc, feature_name, value) VALUES (?, ?, ?, ?)''', vals_to_insert_coef)
    cursor.execute('''INSERT INTO model_params (id, desc, train_score, test_score) VALUES (?, ?, ?, ?)''', vals_to_insert_results)

# Fit model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)

# Save to database
save_to_database(1, 'Baseline model', db, baseline_model, X_train, X_test, y_train, y_test)





