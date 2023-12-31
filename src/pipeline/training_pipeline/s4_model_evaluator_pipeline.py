"""Module to create pipeline to train models"""
from src import logger
from src.components.model.model_evaluator import ModelEvaluator
from src.configuration.configuration_manager import ConfigurationManager


class ModelEvaluatorPipeline():
    """Class to create pipeline to train models"""

    def __init__(self):
        pass

    def evaluate(self):
        """Method to invoke model training"""
        try:
            config = ConfigurationManager()
            model_evaluator = ModelEvaluator(config=config.get_evaluation_config())
            model_evaluator.evaluate_model()
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    try:
        STAGE_NAME = "Model Evaluation stage"
        logger.info("%s started", STAGE_NAME)
        model_evaluator_pipe = ModelEvaluatorPipeline()
        model_evaluator_pipe.evaluate()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as exc:
        logger.exception("Exception occured: %s", exc)
