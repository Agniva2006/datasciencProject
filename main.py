from src.datasciencProject.utils import logger
from src.datasciencProject.pipeline.data_ingestion import DataIngestionPipeline
from src.datasciencProject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datasciencProject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datasciencProject.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datasciencProject.config import configuration
stage_name = "Data Ingestion Stage"

try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj=DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

stage_name=" Data Validation Stage"
try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj=DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.initiate_data_transformation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.initiate_model_training()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e