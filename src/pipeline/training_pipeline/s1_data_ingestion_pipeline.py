"""Module to create data ingestion pipeline"""
from src.configuration.configuration_manager import ConfigurationManager
from src.components.data.data_ingestion import DataIngestion
from src import logger


class DataIngestionPipeline:
    """Class to create data ingestion pipeline"""

    def __init__(self):
        pass

    def ingest(self):
        """Method to perform data ingestion"""
        try:
            config = ConfigurationManager.instance()
            data_ingestion = DataIngestion(config=config.get_data_config())
            data_ingestion.ingest_data()
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info("%s started", STAGE_NAME)
        obj = DataIngestionPipeline()
        obj.ingest()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as exc:
        logger.exception("Exception occured: %s", exc)
