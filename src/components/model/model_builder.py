"""Module to build base models"""
import os
import tensorflow as tf
from src.entities.config_entity import ModelConfig
from src.utils.common import remove_directories
from src import logger


class ModelBuilder():
    """Class to build base models"""

    def __init__(self, config: ModelConfig):
        self.config = config

    def get_base_model(self):
        """Method to get base model"""
        try:
            base_model = tf.keras.applications.vgg16.VGG16(
                input_shape=self.config.params_image_size,
                weights=self.config.params_weights,
                include_top=self.config.params_include_top)
            return base_model
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    @staticmethod
    def update_base_model(model, classes, freeze_all=True, freeze_till=0, learning_rate=0.01):
        """Method to update base model"""
        try:
            if freeze_all:
                for layer in model.layers:
                    layer.trainable = False
            elif freeze_till > 0:
                for layer in model.layers[:-freeze_till]:
                    layer.trainable = False

            flatten_in = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation="softmax")(flatten_in)

            updated_model = tf.keras.models.Model(
                inputs=model.input,
                outputs=prediction)

            updated_model.compile(
                optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=["accuracy"])
            return updated_model
        except Exception as ex:
            raise ex

    def build_model(self):
        """Method to invoke model building"""
        try:
            # Delete existing model
            if os.path.exists(self.config.base_model_path):
                remove_directories(self.config.base_model_path)
                logger.info(
                    "Deleted already present base model. Rebuilding model.")

            # Get base model
            base_model = self.get_base_model()
            
            # Update base model
            model = self.update_base_model(
                model=base_model,
                classes=self.config.params_classes,
                freeze_all=True,
                freeze_till=0,
                learning_rate=self.config.params_learning_rate
            )

            # Save updated base model
            model.save(self.config.base_model_path)
            logger.info("Model built and saved successfully to: %s",
                        self.config.base_model_path)
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
