import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

list_of_files = [
    "application_logging/logger.py",
    "best_model_finder/tuner.py",
    "data_ingestion/data_loader.py",
    "data_ingestion/data_loader_prediction.py",
    "data_preprocessing/clustring.py",
    "data_preprocessing/preprocessing.py",
    "data_transfromation_training/data_transformation.py",
    "data_transfromation_prediction/data_transformation_prediction.py",
    "data_type_validation_insertion_training/datatypevalidation.py",
    "data_type_validation_insertion_prediction/datatypevalidationprediction.py",
    "file_operations/file_methods.py",
    "training_raw_data_validation/rawdatavalidation.py",
    "prediction_raw_data_validation/predictiondatavalidation.py",
    "templates/index.html",
    "main.py",
    "predict_from_model.py",
    "prediction_validation_insertion.py",
    "training_validation_insertion.py",
    "training_model.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Createing directory; {filedir} for the file:{filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists.")