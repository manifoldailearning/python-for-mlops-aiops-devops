from flask import Flask, jsonify, request
import numpy as np
from pathlib import Path
import os 
import sys 
import pathlib
import pickle
import joblib

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))
file_path = 'model/iris_model.joblib'
saved_path = os.path.join(PACKAGE_ROOT,file_path)
model = joblib.load(saved_path)

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X = np.array(data['data'])

    predictions = model.predict(X.tolist()).tolist()  

    return jsonify({'predictions': predictions}) 

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
