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