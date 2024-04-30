#!/usr/bin/env python
import pandas as pd
from pathlib import Path
import os 
import sys 
import joblib

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from src.model import IrisClassifier
from src.data_processing import load_iris_data
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
import pickle
import config

def main():
    data_path = config.file_path 

    df = load_iris_data(data_path)

    X = df.drop('species', axis=1)
    y = df['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = IrisClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Save the model
    joblib.dump(model,'model/iris_model.joblib')

if __name__ == '__main__':
    main()
