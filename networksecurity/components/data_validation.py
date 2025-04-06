import os
import sys
import numpy as np
import pandas as pd
from networksecurity.exception.exception  import NetworkSecurityExecption
from networksecurity.constant import training_pipeline
from networksecurity.logging.logger import logger
from networksecurity.entity.config_enitity import DataValidationConfig
from scipy.stats import ks_2samp
from networksecurity.utilis.main_utilis.utils import read_yaml_file,write_yaml_file
from networksecurity.entity.artifact_entity import DataIngestionArtiacts,DataValidationArtifact
from networksecurity.entity.config_enitity import DataValidationConfig
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtiacts,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact= data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config =read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)
    @staticmethod
    def read_data(file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)
    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns=len(self._schema_config)
            logger.info(f"required number of columns :{number_of_columns}")
            logger.info(f"data fram has columns:{len(dataframe.columns)}")
            if len(dataframe.columns)==number_of_columns:
                return True
            else:
                return False
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)
    def check_if_columns_exist(self, dataframe: pd.DataFrame) -> list:
        try:
            # Extract expected columns from schema
            expected_columns = list(self._schema_config["columns"].keys()) if isinstance(self._schema_config["columns"], dict) else list(self._schema_config["columns"])
            # Extract actual columns from dataframe
            actual_columns = list(dataframe.columns)
            # Identify missing and extra columns
            missing_columns = [col for col in expected_columns if col not in actual_columns]  
            extra_columns = [col for col in actual_columns if col not in expected_columns]  
            # Return a list of all problematic columns
            return missing_columns + extra_columns  
        except Exception as e:
            raise NetworkSecurityExecption(e, sys)
    def let_check_data_drift(self,base_df,current_df,threshold=0.5)->bool:
        try:
            status = True  # Assume no drift initially
            report = {}

            for column in base_df.columns:
                if column in current_df.columns:  # Ensure the column exists in both dataframes
                    d1 = base_df[column]
                    d2 = current_df[column]

                    is_sample_dist = ks_2samp(d1,d2)

                    if threshold <= is_sample_dist.pvalue:
                        is_found = False  # No drift
                    else:
                        is_found = True   # Drift detected
                        status = False
                    
                    report =({column:{
                        "p_value": float(is_sample_dist.pvalue),
                        "drift_status": is_found}})
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            dir_path=os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path,content=report)

            
        except Exception as e:
                raise NetworkSecurityExecption(e,sys)
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path=self.data_ingestion_artifact.trained_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            ##read the data from train nd test
            train_dataframe=DataValidation.read_data(train_file_path)
            test_dataframe=DataValidation.read_data(test_file_path)
            status=self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message=f" train data frame deos not contain all columns.\n"
            status=self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message=f" test data fram deos not contain all columns.\n"
            train_column_issues = self.check_if_columns_exist(dataframe=train_dataframe)
            if train_column_issues:
                error_message += f"Train data has column mismatches: {train_column_issues}\n"
            test_column_issues = self.check_if_columns_exist(dataframe=test_dataframe)
            if test_column_issues:error_message += f"Test data has column mismatches: {test_column_issues}\n"

            status=self.let_check_data_drift(base_df=train_dataframe,current_df=test_dataframe)
            dir_path=os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            train_dataframe.to_csv(
               self.data_validation_config.valid_train_file_path,index=False,header=True)
            test_dataframe.to_csv(
               self.data_validation_config.valid_test_file_path,index=False,header=True)
            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_ingestion_artifact.trained_file_path,
                valid_test_file_path=self.data_ingestion_artifact.test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )
            return data_validation_artifact

        except Exception as e:
            raise NetworkSecurityExecption(e,sys)