import pandas as pd
import os
import sys
import json
FILE_PATH = r"Network_Data\phisingData.csv"
data = pd.read_csv(FILE_PATH)
data.reset_index(drop=True,inplace=True)
print(data.head()) 
records=list(json.loads((data.T.to_json())).values())
print(records)