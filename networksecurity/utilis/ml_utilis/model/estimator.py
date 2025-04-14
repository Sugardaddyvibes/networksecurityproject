from networksecurity.constant.training_pipeline import SAVE_MODEL_DIR,SAVE_MODEL_FILE_NAME
import sys
from networksecurity.exception.exception import NetworkSecurityExecption
from networksecurity.logging.logger import logger
class NetworkModel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor=preprocessor
            self.model=model
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)
    def predict(self,x):
        try:
            x_transform=self.preprocessor.transform(x)
            y_hat=self.nodel.predict(x_transform)
            return y_hat
        except Exception as e:
            raise NetworkSecurityExecption(e,sys)