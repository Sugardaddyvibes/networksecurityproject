from networksecurity.exception.exception  import NetworkSecurityExecption
import sys
import os 
from networksecurity.constant import training_pipeline
from networksecurity.logging.logger import logger
from networksecurity.entity.config_enitity import DataTransformationconfig
from networksecurity.entity.artifact_entity import DataValidationArtifact,DataTransformationArtifact
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from networksecurity.logging.logger import logger
import pandas as pd
import numpy as np
from networksecurity.utilis.main_utilis.utils import save_numpy_array_data,save_object 
from networksecurity.constant.training_pipeline import TARGET_COLUMNS,DATA_TRANSFORMATION_IMPUTER_PARAMS



class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationconfig):
        try:
            self.data_validation_artifact:DataValidationArtifact= data_validation_artifact
            self.data_transformation_config:DataTransformationconfig= data_transformation_config
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)
    @staticmethod
    def read_data(file_path)-> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)
    def get_trandormer_object(cls)->Pipeline:
        """
        It initialises a KNNImputer object with the parameters specified in the training_pipeline.py file
        and returns a Pipeline object with the KNNImputer object as the first step.

        Args:
          cls: DataTransformation

        Returns:
          A Pipeline object
        """
        logger.info(
            "Entered get_data_trnasformer_object method of Trnasformation class"
        )
        try:
            imputer:KNNImputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            loggerinfo:(
                f":intialiase KNNimputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}"
            )
            processor:Pipeline=Pipeline([("imputer",imputer)])
            return processor

        except Exception as e:
            raise NetworkSecurityExecption(e,sys)

    def initiate_data_transformation(self)->DataTransformationArtifact:
        logger.info ('Entred initiate_data_transformation method of DataTransfomation class')

        try:
            logger.info("STARTING  data transformation")
            train_df=DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df =DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            """"
            drop my target column"
            """""
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMNS],axis=1)
            target_feature_train_df=train_df[TARGET_COLUMNS]
            target_feature_train_df=target_feature_train_df.replace(-1,0)


            input_feature_test_df=test_df.drop(columns=[TARGET_COLUMNS],axis=1)
            target_feature_test_df=test_df[TARGET_COLUMNS]
            target_feature_test_df=target_feature_test_df.replace(-1,0)

            preprocessor=self.get_trandormer_object()

            preprocessor_object=preprocessor.fit(input_feature_train_df)
            tranformed_input_feature_train_df=preprocessor_object.transform(input_feature_train_df)
            tranformed_input_feature_test_df=preprocessor_object.transform(input_feature_test_df)
            train_arr=np.c_[tranformed_input_feature_train_df,np.array(target_feature_train_df)]
            test_arr=np.c_[tranformed_input_feature_test_df,np.array(target_feature_test_df)]
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,array=train_arr,)
            save_numpy_array_data( self.data_transformation_config.transformed_test_file_path,array=test_arr,)
            save_object( self.data_transformation_config.transformed_object_file_path,preprocessor_object,)

            save_object("final_model/preprocessor.pkl",preprocessor_object)

            

            #preparing artifacts
            data_transformation_artifact=DataTransformationArtifact(
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_test_file_path= self.data_transformation_config.transformed_test_file_path
            )
            return  data_transformation_artifact


            
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)