import os,sys 
from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d  %H-%M-%S')}"


CURRENT_TIME_STAMP=get_current_time_stamp()

ROOT_DIR_KEY=os.getcwd()
DATA_DIR='DATA'
DATA_DIR_KEY='finalTrain.csv'

ARTIFACT_DIR_KEY='Artifact'

## data ingestion releated variable

DATA_INGESTION_KEY='data_ingestion'
DATA_INGESTION_RAW_DATA_DIR='raw_data_dir'
DATA_INGESTED_DATA_DIR_KEY='Ingested_dir'
RAW_DATA_DIR_KEY='raw.csv'
TRAIN_DATA_DIR_KEY='train.csv'
TEST_DATA_DIR_KEY='test.csv'