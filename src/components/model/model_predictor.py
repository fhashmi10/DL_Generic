
"""Module to perform prediction"""
import numpy as np
import tensorflow as tf
from src.entities.config_entity import TrainConfig
from src import logger


class ModelPredictor:
    """Class to perform prediction"""

    def __init__(self, train_config=TrainConfig):
        self.train_config = train_config

    @staticmethod
    def transform_input_data(file_path):
        """Method to transform input data"""
        try:
            input_image = tf.keras.preprocessing.image.load_img(
                file_path, target_size=(224, 224))
            input_image = tf.keras.preprocessing.image.img_to_array(
                input_image)
            input_image = np.expand_dims(input_image, axis=0)
            return input_image
        except Exception as ex:
            raise ex

    def predict(self, file_path):
        """Method to invoke prediction"""
        try:
            # Transform input data
            input_image = self.transform_input_data(file_path=file_path)

            # Load the model
            model = tf.keras.models.load_model(
                self.train_config.trained_model_path)
            logger.info("loaded model successfully.")

            # Predict
            prediction = np.argmax(model.predict(input_image), axis=1)
            logger.info("Predicted %s", prediction)
            return prediction
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
