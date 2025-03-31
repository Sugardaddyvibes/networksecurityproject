#import pandas as pd
import os
#import sys
#import json
#FILE_PATH = r"Network_Data\phisingData.csv"
#data = pd.read_csv(FILE_PATH)
#data.reset_index(drop=True,inplace=True)
#print(data.head()) 
#records=list(json.loads((data.T.to_json())).values())
#rint(records)import os

# SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

# if not os.path.exists(SCHEMA_FILE_PATH):
#     raise FileNotFoundError(f"Schema file not found at: {SCHEMA_FILE_PATH}")
# else:
#     print(f"Schema file found at: {SCHEMA_FILE_PATH}")
import yaml

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

with open(SCHEMA_FILE_PATH, "r") as file:
    schema_config = yaml.safe_load(file)

print(schema_config)  # 
