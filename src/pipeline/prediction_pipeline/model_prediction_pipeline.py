"""Module to create model prediction pipeline"""
from src.configuration.configuration_manager import ConfigurationManager
from src.components.model.model_predictor import ModelPredictor
from src import logger


class PredictionPipeline:
    """Class to create model prediction pipeline"""

    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        """Method to perform prediction"""
        try:
            config = ConfigurationManager.instance()
            model_predictor = ModelPredictor(train_config=config.get_train_config())
            prediction = model_predictor.predict(self.filename)

            if prediction[0] == 1:
                result = 'Healthy'
            else:
                result = 'Coccidiosis'
            return [{"image": result}]
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
