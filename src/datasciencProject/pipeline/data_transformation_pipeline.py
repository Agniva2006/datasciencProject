from src.datasciencProject.config.configuration import ConfigurationManager
from src.datasciencProject.components.data_transformation import DataTransformationConfig
from src.datasciencProject.utils import logger
from pathlib import Path

STAGE_NAME="Data Transfromation_stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):

            try:
                with open(Path("artifacts/data_validation/status.txt"),'r')  as f:
                     status=f.read().split(" ")[-1]          
                     config=ConfigurationManager()
                if  status==True:
                    config=ConfigurationManager()
                    data_transformation_config=config.get_data_transformation_config()
                    DataTransformationConfig.download_file(config=data_transformation_config)
                    DataTransformationConfig.validate_all_columns()
                else:
                     raise Exception("Your data scheme is not valid")    
                    
            except Exception as e:
                print(e)