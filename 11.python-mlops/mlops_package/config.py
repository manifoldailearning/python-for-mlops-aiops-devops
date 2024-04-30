import pathlib
import os


PACKAGE_ROOT = pathlib.Path(mlops_package.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT,"data","raw")
file_name = "iris.csv"
file_path = os.path.join(DATAPATH,file_name)
MODEL_NAME = 'iris_model.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,'model')

