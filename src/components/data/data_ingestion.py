""""Module to perform data ingestion"""
import os
import urllib.request as request
from src import logger
import zipfile
from src.entities.config_entity import DataConfig
from src.utils.common import create_directories, remove_directories


class DataIngestion():
    """Class to perform data ingestion"""
    def __init__(self, config: DataConfig):
        self.config = config


    def unzip_data(self, unzip_path):
            """Method to unzip data"""
            create_directories([unzip_path])
            with zipfile.ZipFile(self.config.data_download_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Data unzipped successfully!")


    def download_data_from_URL(self, skip_existing=True):
        """Method to download data from URL"""
        download_path=self.config.data_download_path
        download_dir=os.path.dirname(os.path.abspath(download_path))
        create_directories([download_dir])
        if not os.path.exists(download_path):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = download_path
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"Data file already exists, skipping download")
        
        #unzip file
        unzip_path=self.config.data_original_path
        if os.path.exists(unzip_path):
            #option 1: remove existing unzipped files
            if not skip_existing:
                remove_directories(unzip_path)
                self.unzip_data(unzip_path)
            #option 2: skip existing unzipped files
            else:
                logger.info(f"Unzipped data already exists, skipping unzip")
        else:
            self.unzip_data(unzip_path)