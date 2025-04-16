import os
import sys
from  networksecurity.exception.exception import NetworkSecurityExecption
from networksecurity.logging.logger import logger


from networksecurity.components.data_inestion_2 import DataIngestion
from networksecurity.components.data_validation import DataValidation
from  networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.config_enitity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationconfig,
    ModelTranierConfig


)

from networksecurity.entity.artifact_entity import (
    DataIngestionArtiacts,
    DataTransformationArtifact,
    DataValidationArtifact,
    ModelTrainerArtifact
)



class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataIngestion(training_pipeline_config=self.training_pipeline_config)
            logger.info("start data ingestion")
            data_ingestion=DataIngestion(data_ingestation_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logger.info(f"data ingestion completed and artifact:{data_ingestion_artifact}")
            return data_ingestion_artifact
            
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtiacts):
        try:
            data_validation_config=DataValidation(training_pipeline_config=self.training_pipeline_config)
            logger.info("start data validation")
            data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            logger.info("Initiate the data Validation")
            data_validation_artifact=data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e :
            raise NetworkSecurityExecption(e,sys)
    def start_data_transformation(self,data_validation_artifact:DataTransformationArtifact):
        try:
            data_tranformation_config=DataTransformation(training_pipeline_config=self.training_pipeline_config)
            logger.info("start data validation")
            data_tranformation=DataTransformation(data_validation_artifact=data_validation_artifact,data_tranformation_config=data_tranformation_config)
            logger.info("Initiate the data Validation")
            data_validation_artifact=data_tranformation.initiate_data_transformation()
            return data_validation_artifact
        except Exception as e :
            raise NetworkSecurityExecption(e,sys)
    def start_model_trainer(self,data_validation_artifact:DataValidationArtifact):
        try:
            model_trainer_config=ModelTrainer(training_pipeline_config=self.training_pipeline_config)
            logger.info("start data transformation")
            model_trainer=ModelTrainer(data_validation_artifact=data_validation_artifact,model_trainer_config=model_trainer_config)
            logger.info("Initiate the data Validation")
            model_trainer_artifact=model_trainer.initiate_model_trainer()
            return  model_trainer_artifact
        except Exception as e :
            raise NetworkSecurityExecption(e,sys)
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            return model_trainer_artifact

            
        except Exception as e:

            raise NetworkSecurityExecption (e,sys)





