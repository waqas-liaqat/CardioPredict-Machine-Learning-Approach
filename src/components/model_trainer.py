import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

# Metrics and tuning
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "Logistic Regression": (LogisticRegression(random_state=42, max_iter=500, solver="saga"), None),
                "SVC": (SVC(random_state=42), {'kernel': ['rbf', 'poly', 'sigmoid'], 'C': [0.1, 1, 10], 'gamma': [1, 0.1, 0.01]}),
                "DecisionTreeClassifier": (DecisionTreeClassifier(random_state=42), {'max_depth': [None, 5, 10], 'splitter': ['best', 'random']}), 
                "RandomForestClassifier": (RandomForestClassifier(random_state=42), {'n_estimators': [10, 100, 1000], 'max_depth': [None, 5, 10]}),
                "KNeighborsClassifier": (KNeighborsClassifier(), {'n_neighbors': np.arange(3, 30, 2), 'weights': ['uniform', 'distance']}),
                "GradientBoostingClassifier": (GradientBoostingClassifier(random_state=42), {'n_estimators': [10, 100, 1000]}),
                "XGBClassifier": (
                    XGBClassifier(random_state=42),
                    {
                        'n_estimators': [10, 100, 1000],
                        'learning_rate': [0.1, 0.01, 0.001],
                        'max_depth': [3, 6, 9]
                    }
                ),
                "AdaBoostClassifier": (AdaBoostClassifier(random_state=42), {'n_estimators': [50, 100, 200], 'learning_rate': [0.1, 0.5, 1]}),
            }

            # Extract models and parameters separately
            models_dict = {name: model for name, (model, _) in models.items()}
            params_dict = {name: param for name, (_, param) in models.items() if param is not None}

            # Evaluate models
            model_report = evaluate_models(X_train, y_train, X_test, y_test, models_dict, params_dict)

            # Select the best model
            best_model_name, best_model_score = max(model_report.items(), key=lambda x: x[1])
            best_model = models_dict[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No suitable model found with acceptable performance")

            logging.info(f"Best model found: {best_model_name} with score: {best_model_score}")

            # Save best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # Make predictions and evaluate accuracy
            best_model.fit(X_train, y_train)  # Ensure best model is trained
            predicted = best_model.predict(X_test)
            accuracy = accuracy_score(y_test, predicted)

            return accuracy

        except Exception as e:
            raise CustomException(e, sys)
