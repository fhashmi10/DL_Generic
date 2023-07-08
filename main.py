from src import logger
from src.pipeline.training_pipeline.s1_data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.training_pipeline.s2_model_builder_pipeline import ModelBuilderPipeline
from src.pipeline.training_pipeline.s3_model_trainer_pipeline import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Builder stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
   obj = ModelBuilderPipeline()
   obj.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e


STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
   obj = ModelTrainerPipeline()
   obj.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e