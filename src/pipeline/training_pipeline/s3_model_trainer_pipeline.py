"""Module to create model training pipeline"""
from src.configuration.configuration_manager import ConfigurationManager
from src.components.model_callbacks import ModelCallbacks
from src.components.model_trainer import ModelTrainer
from src import logger

class ModelTrainerPipeline:
    """Class to create model training pipeline"""
    def __init__(self):
        pass

    def train(self):
        """Method to perfom model training"""
        config=ConfigurationManager()
        model_callback = ModelCallbacks(config=config.get_callback_config())
        callback_list = model_callback.get_callbacks()

        model_trainer=ModelTrainer(config=config.get_train_config())
        model_trainer.train_model(callback_list=callback_list, training=False)
        model_trainer.evaluate_model()


if __name__ == '__main__':
    STAGE_NAME = "Model Trainer stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.train()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e