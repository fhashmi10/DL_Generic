"""Module to build base models"""
from src.entities.config_entity import ModelConfig
import tensorflow as tf
from src import logger
import os

class ModelBuilder():
    """Class to build base models"""
    def __init__(self, config: ModelConfig):
        self.config = config
        self.base_model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

    
    @staticmethod
    def update_base_model(model, classes, freeze_all=True, freeze_till=0, learning_rate=0.01):
        """Method to update base model"""
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif freeze_till > 0:
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        #full_model.summary()
        return full_model
    

    def build_model(self):
        """Method to invoke model building"""
        if os.path.exists(self.config.base_model_path):
            logger.info(f"Model built already, skipping build")
        else:
            self.model = self.update_base_model(
                model=self.base_model,
                classes=self.config.params_classes,
                freeze_all=True,
                freeze_till=0,
                learning_rate=self.config.params_learning_rate
            )
            self.model.save(self.config.base_model_path)
            logger.info(f"Model built and saved successfully to {self.config.base_model_path}")

    
   

    


