""""Module to create data generator"""
import tensorflow as tf
from src import logger
from src.singleton import Singleton


@Singleton
class DataGenerator():
    """Class to create data generator"""

    def __init__(self):
        logger.info("Initializing Data Generator. This should only happen once.")
        self.train_generator: tf.keras.preprocessing.image.DirectoryIterator
        self.valid_generator: tf.keras.preprocessing.image.DirectoryIterator

    @staticmethod
    def get_datagenerator_kwargs() -> dict:
        """Method to get the datagenerator kwarg"""
        try:
            return {"rescale": 1./255,
                    "validation_split": 0.20}
        except Exception as ex:
            logger.exception("Error getting datagenerator kwargs: %s", ex)
            raise ex

    @staticmethod
    def get_dataflow_kwargs(config) -> dict:
        """Method to get the datagenerator kwarg"""
        try:
            return {"target_size": config.params_image_size[:-1],
                    "batch_size": config.params_batch_size,
                    "interpolation": "bilinear"}
        except Exception as ex:
            logger.exception("Error getting dataflow kwargs: %s", ex)
            raise ex

    @staticmethod
    def get_dataaug_kwargs() -> dict:
        """Method to get the datagenerator kwarg"""
        try:
            return {"rotation_range": 40,
                    "horizontal_flip": True,
                    "width_shift_range": 0.2,
                    "height_shift_range": 0.2,
                    "shear_range": 0.2,
                    "zoom_range": 0.2}
        except Exception as ex:
            logger.exception("Error getting dataaug kwargs: %s", ex)
            raise ex

    def create_image_data_generator(self, config):
        """Method to invoke the creation of image data generator"""
        try:
            # Get keyword arguments
            dataaug_kwargs = self.get_dataaug_kwargs()
            datagenerator_kwargs = self.get_datagenerator_kwargs()
            dataflow_kwargs = self.get_dataflow_kwargs(config)

            # Define image data generator
            if config.params_is_augmentation:
                imagedatagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                    **dataaug_kwargs,
                    **datagenerator_kwargs
                )
            else:
                imagedatagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                    **datagenerator_kwargs
                )

            self.train_generator = imagedatagenerator.flow_from_directory(
                directory=config.training_data_path,
                subset="training",
                shuffle=True,
                **dataflow_kwargs
            )

            self.valid_generator = imagedatagenerator.flow_from_directory(
                directory=config.training_data_path,
                subset="validation",
                shuffle=False,
                **dataflow_kwargs
            )
            return imagedatagenerator
        except AttributeError as ex:
            logger.exception("Error creating image generator.")
            raise ex
        except Exception as ex:
            raise ex

    def get_train_generator(self) -> tf.keras.preprocessing.image.DirectoryIterator:
        """Method to get the image generator train subset"""
        try:
            return self.train_generator
        except Exception as ex:
            logger.exception("Error getting train image generator.")
            raise ex

    def get_valid_generator(self) -> tf.keras.preprocessing.image.DirectoryIterator:
        """Method to get the image generator valid subset"""
        try:
            return self.valid_generator
        except Exception as ex:
            logger.exception("Error getting valid image generator.")
            raise ex
