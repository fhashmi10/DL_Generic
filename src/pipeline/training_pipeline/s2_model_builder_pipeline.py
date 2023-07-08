from src.config.config_manager import ConfigurationManager
from src.components.model_builder import ModelBuilder
from src import logger

class ModelBuilderPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_builder=ModelBuilder(config=config.get_model_config())
        model_builder.build_model()


if __name__ == '__main__':
    STAGE_NAME = "Model Builder stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelBuilderPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e