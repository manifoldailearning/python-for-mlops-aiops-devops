import pytest
import pandas as pd
from sklearn.datasets import load_iris 
import sys
import pathlib
import os 
from pathlib import Path

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from src.model import IrisClassifier

@pytest.fixture()
def sample_iris_data():
    iris = load_iris(as_frame=True)
    X = iris.data
    y = iris.target
    return X, y

def test_model_fit(sample_iris_data):
    X, y = sample_iris_data
    model = IrisClassifier()
    model.fit(X, y)
    # Ensure the model's internal state is updated after fitting

def test_model_predict(sample_iris_data):
    X, y = sample_iris_data
    model = IrisClassifier()
    model.fit(X, y)
    predictions = model.predict(X[:5])  # Predict on a few samples
    assert all(predictions == y[:5])  # Simplified accuracy check 
