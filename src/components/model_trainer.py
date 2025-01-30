import os
import sys
from dataclasses import dataclass

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

# Metrics and tuning
from sklearn.metrics import accuracy_score

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Logistic Regression": LogisticRegression(random_state=42),
                "SVC": SVC(random_state=42),
                "Decision Tree": DecisionTreeClassifier(random_state=42),
                "Random Forest": RandomForestClassifier(random_state=42),
                "K-Nearest Neighbors": KNeighborsClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(random_state=42),
                "XGBClassifier": XGBClassifier(random_state=42, objective='multi:softprob', num_class=len(y_train.unique())),
                "AdaBoost": AdaBoostClassifier(random_state=42),
            }

            params = {
                "Logistic Regression": {},
                "SVC": {
                    'kernel': ['rbf', 'poly', 'sigmoid'],
                    'C': [0.1, 1, 10],
                    'gamma': [1, 0.1, 0.01]
                },
                "Decision Tree": {
                    'max_depth': [None, 5, 10],
                    'splitter': ['best', 'random']
                },
                "Random Forest": {
                    'n_estimators': [10, 100, 1000],
                    'max_depth': [None, 5, 10]
                },
                "K-Nearest Neighbors": {
                    'n_neighbors': np.arange(3, 30, 2),
                    'weights': ['uniform', 'distance']
                },
                "Gradient Boosting": {
                    'n_estimators': [10, 100, 1000]
                },
                "XGBClassifier": {
                    'n_estimators': [10, 100, 1000],
                    'learning_rate': [0.1, 0.01, 0.001],
                    'max_depth': [3, 6, 9]
                },
                "AdaBoost": {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.1, 0.5, 1]
                }
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models,param=params)
            
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            accuracy = accuracy_score(y_test, predicted)
            return accuracy
            



            
        except Exception as e:
            raise CustomException(e,sys)