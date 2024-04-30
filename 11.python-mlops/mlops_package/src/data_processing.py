import pandas as pd

def load_iris_data(data_path):
    df = pd.read_csv(data_path)
    return df
