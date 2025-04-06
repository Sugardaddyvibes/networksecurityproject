import os
import sys
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from sklearn.model_selection import train_test_split
from networksecurity.exception.exception  import NetworkSecurityExecption
from networksecurity.logging.logger import logger   
from dotenv import load_dotenv
import pymongo.mongo_client
from pymongo import MongoClient
from networksecurity.constant import training_pipeline
from networksecurity.logging.logger import logger
from networksecurity.entity.config_enitity import DataIngestionConfig,TrainingPipelineConfig
from networksecurity.constant import training_pipeline 
from networksecurity.entity.artifact_entity import DataIngestionArtiacts 

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

class  DataIngestion:
    def __init__(self,data_ingestation_config:DataIngestionConfig):
       try:
           self.data_ingestation_config=data_ingestation_config
       except Exception as e:
           raise NetworkSecurityExecption(e,sys)
       
    def import_collection_as_dataframe(self):
        try:
            database_name=self.data_ingestation_config.database_name
            collection_name=self.data_ingestation_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection= self.mongo_client[database_name][collection_name]
            
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"],axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        feature_store_file_path=self.data_ingestation_config.feature_store_file_path

        dir_path = os.path.dirname(feature_store_file_path)
        os.makedirs(dir_path,exist_ok=True)
        dataframe.to_csv(feature_store_file_path,index=False,header=True)
        return dataframe
    def train_test_split_data(self,dataframe:pd.DataFrame):
        train_set, test_set=train_test_split(dataframe,test_size=self.data_ingestation_config.train_test_split_ratio,random_state=42)
        logger.info("train_test_split succesfully done")


        logger.info("exited the train_split method of the data ingesttion class")
        dir_path = os.path.dirname(self.data_ingestation_config.training_file_path)
        os.makedirs(dir_path,exist_ok=True)
        logger.info("exporting rain and test_file path")
        train_set.to_csv(self.data_ingestation_config.training_file_path,index=False,header=True)
        test_set.to_csv(self.data_ingestation_config.testing_file_path,index=False,header=True)





    
    
    def initiate_data_ingestion(self):
        try:
            dataframe=self.import_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe) 
            self.train_test_split_data(dataframe)
            dataingestionartiacts=DataIngestionArtiacts(
                trained_file_path=self.data_ingestation_config.training_file_path,
                test_file_path=self.data_ingestation_config.testing_file_path)   
            return dataingestionartiacts


        except Exception as e:
            raise NetworkSecurityExecption(e,sys)
