"""Module to map data from config to dataclasses"""
import os
from pathlib import Path
from ensure import EnsureError
from src.configuration import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.utils.common import read_yaml_configbox
from src.entities.config_entity import DataConfig, ModelConfig, CallbackConfig, TrainConfig
from src import logger


class ConfigurationManager:
    """Class to manage configuration"""

    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):
        try:
            self.config = read_yaml_configbox(config_file_path)
            self.params = read_yaml_configbox(params_file_path)
        except EnsureError as ex:
            logger.exception("Problem reading parameters yaml file.")
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex

    def get_data_config(self) -> DataConfig:
        """Method to manage data configuration"""
        try:
            config = self.config.data
            data_config = DataConfig(source_url=config.source_url,
                                     data_download_path=config.data_download_path,
                                     data_original_path=config.data_original_path,
                                     data_transformed_path=config.data_transformed_path)
            return data_config
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex

    def get_model_config(self) -> ModelConfig:
        """Method to manage model configuration"""
        try:
            config = self.config.model
            model_config = ModelConfig(base_model_path=config.base_model_path,
                                       params_image_size=self.params.IMAGE_SIZE,
                                       params_learning_rate=self.params.LEARNING_RATE,
                                       params_include_top=self.params.INCLUDE_TOP,
                                       params_weights=self.params.WEIGHTS,
                                       params_classes=self.params.CLASSES)
            return model_config
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex

    def get_callback_config(self) -> CallbackConfig:
        """Method to manage call back configuration"""
        try:
            config = self.config.callback
            callback_config = CallbackConfig(callback_path=config.callback_path,
                                             tensorboard_log_path=config.tensorboard_log_path,
                                             model_checkpoint_path=config.model_checkpoint_path)
            return callback_config
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex

    def get_train_config(self) -> TrainConfig:
        """Method to manage training configuration"""
        try:
            config = self.config.train
            training_data_path = Path(os.path.join(
                self.config.data.data_original_path, "."))#Chicken-fecal-images
            train_config = TrainConfig(base_model_path=self.config.model.base_model_path,
                                       trained_model_path=config.trained_model_path,
                                       training_data_path=training_data_path,
                                       params_epochs=self.params.EPOCHS,
                                       params_batch_size=self.params.BATCH_SIZE,
                                       params_is_augmentation=self.params.AUGMENTATION,
                                       params_image_size=self.params.IMAGE_SIZE)
            return train_config
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
