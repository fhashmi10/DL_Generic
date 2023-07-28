"""Module to train models"""
from pathlib import Path
import tensorflow as tf
from src.configuration.configuration_manager import TrainConfig
from src.utils.common import save_json

class ModelTrainer():
    """Class to train models"""
    def __init__(self, config=TrainConfig):
        self.config = config

    
    def get_base_model(self):
        """Method to get the base model"""
        self.model=tf.keras.models.load_model(self.config.base_model_path)

    
    def train_valid_generator(self):
        """Method to create train and validation generators"""
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20 #split for validation set
            )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
            )

        dataaug_kwargs = dict(
            rotation_range=40,
            horizontal_flip=True,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2
            )
        

        if self.config.params_is_augmentation:
            imagedatagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                **dataaug_kwargs,
                **datagenerator_kwargs
            )
        else:
            imagedatagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
            )

        self.train_generator = imagedatagenerator.flow_from_directory(
            directory=self.config.training_data_path,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )
        self.valid_generator = imagedatagenerator.flow_from_directory(
            directory=self.config.training_data_path,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        

    def train_model(self, callback_list: list, training=True):
        """Method to invoke model training"""
        self.get_base_model()
        self.train_valid_generator()

        if training:
            self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
            self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size
            self.model.fit(self.train_generator,
                epochs=self.config.params_epochs,
                steps_per_epoch=self.steps_per_epoch,
                validation_steps=self.validation_steps,
                validation_data=self.valid_generator,
                callbacks=callback_list
            )
            self.model.save(self.config.trained_model_path)
        else:
            # todo: check path exists - if not load base and do training again
            self.model=tf.keras.models.load_model(self.config.trained_model_path)
        

    def evaluate_model(self):
        """Method to invoke model evaluation"""
        self.score = self.model.evaluate(self.valid_generator)
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(file_path=Path("scores.json"), data=scores)