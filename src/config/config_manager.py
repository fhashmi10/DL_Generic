from src.config import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.common.utils import read_yaml
from src.entities.config_entity import DataConfig

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        
    def get_data_config(self)-> DataConfig:
        config=self.config.data
        data_config=DataConfig(source_URL=config.source_URL, 
                               data_download_path=config.data_download_path, 
                               data_original_path=config.data_original_path, 
                               data_transformed_path=config.data_transformed_path)
        return data_config
