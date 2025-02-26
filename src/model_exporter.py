# creates a folder
from pathlib import Path
import joblib

class ModelExporter:
    def __init__(self):
        pass

    def create_folder(self, folder_location):
        Path(folder_location).mkdir(exist_ok=True)

    def export_model(self, trained_model, model_name:str):
        joblib.dump(trained_model, f'../{model_name}.pkl')