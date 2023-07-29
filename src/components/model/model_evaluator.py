"""Module to evaluate models"""
from pathlib import Path
import tensorflow as tf
from src.configuration.configuration_manager import TrainConfig
from src.components.data.data_generator import DataGenerator
from src.utils.common import save_json
from src import logger


class ModelEvaluator():
    """Class to evaluate models"""

    def __init__(self, config=TrainConfig):
        self.config = config

    def get_trained_model(self):
        """Method to get the base model"""
        try:
            return tf.keras.models.load_model(self.config.trained_model_path)
        except AttributeError as ex:
            logger.exception("Error loading trained model.")
            raise ex
        except Exception as ex:
            raise ex

    def evaluate_model(self):
        """Method to invoke model training"""
        # Get base model
        try:
            # Get trained model
            model = self.get_trained_model()

            # Get valid generator
            image_data_generator = DataGenerator.instance()
            valid_generator = image_data_generator.get_valid_generator()

            # Evaluate
            score = model.evaluate(valid_generator)
            scores = {"loss": score[0], "accuracy": score[1]}
            save_json(file_path=Path("scores.json"), data=scores)
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
