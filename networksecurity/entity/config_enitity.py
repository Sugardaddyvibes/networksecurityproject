from datetime import datetime
import os
from networksecurity.constant import training_pipeline
print(training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR)
print(training_pipeline.DATA_INGESTION_COLLECTION_NAME)

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
       timeestamp=timestamp.strftime('%m_%d_%Y_%H_%M_%S')
       self.pipeline_name=training_pipeline.PIPELINE_NAME
       self.artifact_name=training_pipeline.ARTIFACT_DIR
       self.artifact_dir=os.path.join(self.artifact_name,timeestamp)
       self.timestamp:str=timeestamp
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestation_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path=os.path.join(
        self.data_ingestation_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR
        )
        self.raw_data_file_path=os.path.join(
        self.data_ingestation_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.RAW_FILE
        )
        self.training_file_path=os.path.join(
        self.data_ingestation_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME
        )
        self.testing_file_path=os.path.join(
        self.data_ingestation_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME
        )
        self.raw_data_file_path=os.path.join(
        self.data_ingestation_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.RAW_FILE
        )
        self.collection_name=training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.train_test_split_ratio= training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.database_name=training_pipeline.DATA_INGESTION_DATABASE_NAME




