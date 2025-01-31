import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
# Metrics and tuning
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    results = {}

    for name, model in models.items():
        try:
            best_model = model  # Default to original model
            best_params = None  # Default to no tuning
            
            if name in params and params[name]:  # If hyperparameters exist
                gs = GridSearchCV(model, params[name], cv=5, scoring='accuracy', n_jobs=-1)
                gs.fit(X_train, y_train)
                best_model = gs.best_estimator_
                best_params = gs.best_params_
            else:
                best_model.fit(X_train, y_train)

            y_pred = best_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            results[name] = accuracy  # Store only accuracy in dictionary
            print(f"{name}: {accuracy:.4f} with params: {best_params}")

        except Exception as e:
            print(f"Error with model {name}: {e}")

    return results  # Ensure we return a dict of model accuracies
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)