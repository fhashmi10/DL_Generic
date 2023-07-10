from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.common.utils import decodeImage
from src.pipeline.prediction_pipeline.model_prediction_pipeline import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.predictor = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def train():
    os.system("python main.py")
    return "Training done successfully!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predict():
    image = request.json['image']
    decodeImage(image, client_appp.filename)
    result = client_appp.predictor.predict()
    return jsonify(result)


if __name__ == "__main__":
    client_appp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #local host
    #app.run(host='0.0.0.0', port=8080) #for AWS
    #app.run(host='0.0.0.0', port=80) #for AZURE

