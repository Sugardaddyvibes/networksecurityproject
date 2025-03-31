import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from sklearn.model_selection import train_test_split
from networksecurity.exception.exception  import NetworkSecurityExecption
from networksecurity.logging.logger import logger   
from dotenv import load_dotenv
import pymongo.mongo_client
from pymongo import MongoClient
from typing import List
from networksecurity.constant import training_pipeline
from networksecurity.logging.logger import logger
from networksecurity.entity.config_enitity import DataIngestionConfig,TrainingPipelineConfig
from networksecurity.constant import training_pipeline 

# Create an instance of TrainingPipelineConfig
training_pipeline_config = TrainingPipelineConfig()

# Create an instance of DataIngestionConfig
data_ingestion_config = DataIngestionConfig(training_pipeline_config)




load_dotenv()
MONGO_DB_URL= os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)



class  DataIngestion:
    def __init__(self):
        try:
            self.client= MongoClient(
              MONGO_DB_URL)
            print("✅ MongoDB Connection Successful!")
            self.database = self.client[training_pipeline.DATA_INGESTION_DATABASE_NAME]
            self.collection = self.database[training_pipeline.DATA_INGESTION_COLLECTION_NAME]
        except Exception as e:
            print(f"❌ MongoDB Connection Failed: {e}")
    def initiate_data_ingestion(self):
        try:
            data=list(self.collection.find())
            if not data:
                raise ValueError("NO data found in the mogodb collection")
            for record in data:
                record.pop('_id',None)

            df=pd.DataFrame(data)
            os.makedirs(os.path.dirname(data_ingestion_config.training_file_path),exist_ok=True)
            print("Creating directory:", os.path.dirname(data_ingestion_config.training_file_path))
            df.to_csv(data_ingestion_config.raw_data_file_path,index=False,header=True)
            logger.info('Train test split intiated')
            train_set,test_set=train_test_split(df,test_size=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION,random_state=42)
            train_set.to_csv(data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(data_ingestion_config.testing_file_path,index=False,header=True)
            logger.info('ingestion of the data is complete')

            return(
                    data_ingestion_config.training_file_path,
                    data_ingestion_config.testing_file_path
               )
        except Exception as e:
           raise NetworkSecurityExecption(e, sys)
        
if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()