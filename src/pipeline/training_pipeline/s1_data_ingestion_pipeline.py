"""Module to create data ingestion pipeline"""
from src.configuration.configuration_manager import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src import logger

class DataIngestionPipeline:
    """Class to create data ingestion pipeline"""
    def __init__(self):
        pass

    def ingest(self):
        """Method to perform data ingestion"""
        config=ConfigurationManager()
        data_ingestion=DataIngestion(config=config.get_data_config())
        data_ingestion.download_data_from_URL()


if __name__ == '__main__':
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.ingest()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e