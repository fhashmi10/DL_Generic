"""Module to create model training pipeline"""
from src.configuration.configuration_manager import ConfigurationManager
from src.components.model.model_callbacks import ModelCallbacks
from src.components.model.model_trainer import ModelTrainer
from src import logger

class ModelTrainerPipeline:
    """Class to create model training pipeline"""
    def __init__(self):
        pass

    def train(self):
        """Method to perfom model training"""
        try:
            config=ConfigurationManager()
            model_callback = ModelCallbacks(config=config.get_callback_config())
            callback_list = model_callback.get_callbacks()

            model_trainer=ModelTrainer(config=config.get_train_config())
            model_trainer.train_model(callback_list=callback_list, training=False)
            model_trainer.evaluate_model()
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    STAGE_NAME = "Model Trainer stage"
    try:
        logger.info("%s started", STAGE_NAME)
        obj = ModelTrainerPipeline()
        obj.train()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as exc:
        logger.exception("Exception occured: %s", exc)
