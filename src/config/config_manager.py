from src.config import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.common.utils import read_yaml
from src.entities.config_entity import DataConfig, ModelConfig

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

    def get_model_config(self)-> ModelConfig:
        config=self.config.model
        model_config=ModelConfig(base_model_path=config.base_model_path,
                                 trained_model_path=config.trained_model_path,
                                 params_image_size=self.params.IMAGE_SIZE,
                                 params_learning_rate=self.params.LEARNING_RATE,
                                 params_include_top=self.params.INCLUDE_TOP,
                                 params_weights=self.params.WEIGHTS,
                                 params_classes=self.params.CLASSES)
        return model_config