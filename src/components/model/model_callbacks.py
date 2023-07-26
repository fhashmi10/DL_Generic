"""Module to perform callbacks"""
from src.entities.config_entity import CallbackConfig
import tensorflow as tf
import time
import os

class ModelCallbacks():
    """Class to perform callbacks"""
    def __init__(self, config: CallbackConfig):
        self.config = config

    
    @property
    def _create_tb_callbacks(self):
        """Property to hold tensorboard log details"""
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_log_path,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    

    @property
    def _create_ckpt_callbacks(self):
        """Property to hold model checkpoints"""
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.model_checkpoint_path,
            save_best_only=True
        )


    def get_callbacks(self):
        """Method to invoke callbacks"""
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]

