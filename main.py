import sys
import os
from networksecurity.components.data_inestion_2  import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception  import NetworkSecurityExecption
from networksecurity.logging.logger import logger
from networksecurity.entity.config_enitity import DataIngestionConfig,DataValidationConfig,DataTransformationconfig
from networksecurity.entity.config_enitity import TrainingPipelineConfig

if __name__ == "__main__":
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(trainingPipelineConfig)
        obj=DataIngestion(dataIngestionConfig)
        logger.info("start data_ingestion")
        dataingestionartifacts=obj.initiate_data_ingestion()
        logger.info("data intiation completed")
        print(dataingestionartifacts)
        logger.info("start data validation")
        data_validation_config=DataValidationConfig(trainingPipelineConfig)
        data_validation=DataValidation(dataingestionartifacts,data_validation_config)
        logger.info("initiate data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logger.info("data  validation  completed")
        print(data_validation_artifact)
        logger.info("start data transformation")
        data_tranformation_config=DataTransformationconfig(trainingPipelineConfig)
        data_transformation=DataTransformation(data_validation_artifact,data_tranformation_config)
        logger.info("initiate data transfromatiom")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logger.info("data  tranformation  completed")
        print(data_transformation_artifact)

        

    except Exception as e:
        raise NetworkSecurityExecption(e,sys)