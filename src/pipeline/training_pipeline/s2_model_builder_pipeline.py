"""Module to create model building pipeline"""
from src.configuration.configuration_manager import ConfigurationManager
from src.components.model.model_builder import ModelBuilder
from src import logger

class ModelBuilderPipeline:
    """Class to create model building pipeline"""
    def __init__(self):
        pass

    def build(self):
        """Method to build model"""
        try:
            config=ConfigurationManager.instance()
            model_builder=ModelBuilder(config=config.get_model_config())
            model_builder.build_model()
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    STAGE_NAME = "Model Builder stage"
    try:
        logger.info("%s started", STAGE_NAME)
        obj = ModelBuilderPipeline()
        obj.build()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as exc:
        logger.exception("Exception occured: %s", exc)
