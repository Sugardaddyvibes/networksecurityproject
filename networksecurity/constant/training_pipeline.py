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



""""
Data ingestion realated constant start with DATA INGESTION VAR NAME"
"""
DATA_INGESTION_COLLECTION_NAME:str= "NetworkData"
DATA_INGESTION_DATABASE_NAME:str="yeritheplug"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str='feature_store'
DATA_INGESTION_INGESTED_DIR:str='ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2
