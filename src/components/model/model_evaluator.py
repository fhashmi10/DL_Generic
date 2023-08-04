"""Module to evaluate models"""
from urllib.parse import urlparse
import mlflow
import tensorflow as tf
from src.entities.config_entity import EvaluationConfig
from src.components.data.data_generator import DataGenerator
from src.utils.common import save_json
from src import logger


class ModelEvaluator():
    """Class to evaluate models"""

    def __init__(self, config=EvaluationConfig):
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

    def log_mlflow(self, model, model_score: dict):
        """Method to log to MLflow"""
        try:
            # Below URL can be used to save experiments on remote server (dagshub can be used)
            # dagshub uri, username and password will need to be
            # exported as env variabls using gitbash terminal
            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_url_type_store = urlparse(
                mlflow.get_tracking_uri()).scheme

            with mlflow.start_run():
                mlflow.log_params(self.config.track_params)
                mlflow.log_metric("loss", model_score["loss"])
                mlflow.log_metric("accuracy", model_score["accuracy"])

                # Model registry does not work with file store
                if tracking_url_type_store != "file":
                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(
                        model, "model", registered_model_name="abc")
                else:
                    mlflow.sklearn.log_model(model, "model")
        except AttributeError as ex:
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
            model_score = model.evaluate(valid_generator)
            result = {"loss": model_score[0], "accuracy": model_score[1]}
            save_json(
                file_path=self.config.evaluation_score_json_path, data=result)

            # Log ml flow
            self.log_mlflow(model, result)
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
