import os
import numpy as np 
import pandas as pd

TARGET_COLUMNS="Result"
FILE_NAME:str="phisingData.csv"
ARTIFACT_DIR:str="Artifacts"
PIPELINE_NAME:str="NetworkSecurity"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"
RAW_FILE:str="raw.csv"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH= os.path.join("data_schema","schema.yaml")



""""
Data ingestion realated constant start with DATA INGESTION VAR NAME"
"""
DATA_INGESTION_COLLECTION_NAME:str= "NetworkData"
DATA_INGESTION_DATABASE_NAME:str="yeritheplug"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str='feature_store'
DATA_INGESTION_INGESTED_DIR:str='ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2

""""
Data validation realated constant start with DATA INGESTION VAR NAME"
"""
DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_VALID_DIR:str='validated'
DATA_VALIDATION_INVALID_DIR:str='invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR:str='drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"

""""
Data transformation   realated constant start with DATA TRANSFROMATION VAR NAME"
"""""
DATA_TRANSFORMATION__DIR_NAME:str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str="data_transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str='tranformed_object'
DATA_TRANSFORMATION_TRAIN_FILE_PATH:str='tran.npy'
DATA_TRANSFORMATION_TEST_FILE_PATH:str='test.npy'
## kkn imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
MODEL_TRAINER_DIR:str="model_trainer"
MODEL_TRAINER_TRAINED_DIR:str="trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str="model.pkl"
MODEL_TRAINER_EXPECTED_SCORE:float=0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05

SAVE_MODEL_DIR:str=os.path.join("saved_models")
SAVE_MODEL_FILE_NAME:str="model.pkl"



