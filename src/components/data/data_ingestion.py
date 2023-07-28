""""Module to perform data ingestion"""
import os
from pathlib import Path
import urllib.request as request
import zipfile
from src.entities.config_entity import DataConfig
from src.utils.common import create_directories, remove_directories
from src import logger


class DataIngestion():
    """Class to perform data ingestion"""

    def __init__(self, config: DataConfig):
        self.config = config

    def download_data_from_url(self):
        """Method to download data from URL"""
        try:
            download_path = self.config.data_download_path
            if not os.path.exists(download_path):
                create_directories([download_path], is_file_path=True)
                file_name, headers = request.urlretrieve(
                    url=self.config.source_url,
                    filename=download_path
                )
                logger.info("%s download! with following info: \n%s",
                            file_name, headers)
            else:
                logger.info("Data file already exists, skipping download.")
        except AttributeError as ex:
            logger.exception("Error downloading data from URL")
            raise ex
        except Exception as ex:
            raise ex

    @staticmethod
    def skip_processing(data_path: Path, skip_existing: bool) -> bool:
        """Method to determine if need to skip processing"""
        try:
            skip_process: bool = False
            if os.path.exists(data_path):
                # skip existing unzipped files
                if skip_existing:
                    logger.info(
                        "Unzipped data already exists, skipping unzip.")
                    skip_process = True
                # remove existing unzipped files
                else:
                    remove_directories(data_path)
            return skip_process
        except Exception as ex:
            raise ex

    def unzip_data(self, unzip_path):
        """Method to unzip data"""
        try:
            create_directories([unzip_path])
            with zipfile.ZipFile(self.config.data_download_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info("Data unzipped successfully.")
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def ingest_data(self, skip_existing=True):
        """Method to ingest data"""
        try:
            # Download data
            self.download_data_from_url()
            # Check if need to skip processing
            skip_processing = self.skip_processing(
                data_path=self.config.data_original_path,
                skip_existing=skip_existing)
            # Unzip downloaded data
            if not skip_processing:
                self.unzip_data(self.config.data_original_path)
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
