import numpy as np
import tensorflow as tf
import os
from src.config.config_manager import ConfigurationManager


class PredictionPipeline:
    def __init__(self,filename):
        self.filename=filename


    def predict(self):
        config=ConfigurationManager()
        model = tf.keras.models.load_model(config.get_train_config().trained_model_path)
        test_image = tf.keras.preprocessing.image.load_img(self.filename, target_size = (224,224))
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
        else:
            prediction = 'Coccidiosis'

        return [{ "image" : prediction}]
