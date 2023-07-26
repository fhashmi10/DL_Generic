"""
main module
"""
from src import logger
from src.pipeline.training_pipeline.s1_data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.training_pipeline.s2_model_builder_pipeline import ModelBuilderPipeline
from src.pipeline.training_pipeline.s3_model_trainer_pipeline import ModelTrainerPipeline

try:
    STAGE_NAME = "Data Ingestion stage"
    logger.info("%s started", STAGE_NAME)
    data_ingestion = DataIngestionPipeline()
    data_ingestion.ingest()
    logger.info("%s completed\nx==========x", STAGE_NAME)

    STAGE_NAME = "Model Building stage"
    logger.info("%s started", STAGE_NAME)
    obj = ModelBuilderPipeline()
    obj.build()
    logger.info("%s completed\nx==========x", STAGE_NAME)

    STAGE_NAME = "Model Training stage"
    logger.info("%s started", STAGE_NAME)
    obj = ModelTrainerPipeline()
    obj.train()
    logger.info("%s completed\nx==========x", STAGE_NAME)
except Exception as ex:
    logger.exception("Exception in processing: %s", ex)
