import sys
import os
from networksecurity.components.data_inestion_2  import DataIngestion
from networksecurity.exception.exception  import NetworkSecurityExecption
from networksecurity.logging.logger import logger
from networksecurity.entity.config_enitity import DataIngestionConfig
from networksecurity.entity.config_enitity import TrainingPipelineConfig
from networksecurity.entity.artifacts_entity import DataIngestionArtiacts

if __name__ == "__main__":
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(trainingPipelineConfig)
        obj=DataIngestion(dataIngestionConfig)
        logger.info("start data_ingestion")
        dataingestionartifacts=obj.initiate_data_ingestion()
        print(dataingestionartifacts)
    except Exception as e:
        raise NetworkSecurityExecption(e,sys)