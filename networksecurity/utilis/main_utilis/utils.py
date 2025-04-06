import yaml 
import numpy as np
import pandas as pd
from networksecurity.exception.exception  import NetworkSecurityExecption
from networksecurity.logging.logger import logger   
import pickle
import os,sys

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityExecption(e, sys) from e

    except Exception as e:
        NetworkSecurityExecption(e,sys)
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityExecption(e, sys)
def save_numpy_array_data(file_path:str,array:np.array):
    """""
    save numpy array data to file 
    file_path:str location of file to save
    array:np.array data to save
    """"" 

    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecurityExecption(e, sys)
    
def save_object(file_path:str,obj:object)-> None:
    
    try:
        logger.info("entered the  save_bject method of the mainutilis class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logger.info("exited the  save_bject method of the mainutilis class")
    except Exception as e:
        raise NetworkSecurityExecption(e, sys)