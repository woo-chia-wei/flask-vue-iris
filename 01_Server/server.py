from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sklearn import svm
import pickle
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def get_model_path(filename):
    current_script_filename = os.path.realpath(__file__)
    current_script_dir = os.path.dirname(current_script_filename)
    return os.path.join(current_script_dir, 'model', filename)

###############################################################
# Iris API:
#   Predict class of flower given sepal and petal information
# Parameters:
#   sepal_length: float
#   sepal_width: float
#   petal_length: float
#   petal_width: float
# Example:
#   URL: http://localhost:5000/api/v1/iris/predict?sepal_length=6.5&sepal_width=3&petal_length=5.8&petal_width=2
#   Output: {"class": "virginica"}
###############################################################

iris_model_filename = 'iris_model.pkl'
iris_params = [
    'sepal_length', 
    'sepal_width',
    'petal_length', 
    'petal_width'
]
iris_params_conversion = [
    float,
    float,
    float,
    float
]
iris_classes = ['setosa', 'versicolor', 'virginica']

def predict_iris(model, data):
    feature = []
    for param in iris_params:
        feature.append(data[param])
    pred = model.predict([feature])[0]
    return {
        'input': data,
        'output': iris_classes[pred]
    }

@app.route('/api/v1/iris/predict', methods=['GET'])
@cross_origin()
def get_iris_prediction():
    with open(get_model_path(iris_model_filename), "rb") as file:
        model = pickle.load(file)
    
    args = request.args
    data = {}
    for param, convert in zip(iris_params, iris_params_conversion):
        data[param] = convert(args[param])

    return jsonify(predict_iris(model, data))

###############################################################

if __name__ == '__main__':
    app.run(debug=True)