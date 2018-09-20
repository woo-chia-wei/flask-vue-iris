# About

Prototype of analytic API explorer with Frontend using [Vue JS](https://vuejs.org/) and Backend using [Flask](http://flask.pocoo.org/).

# Instruction

1. Run `00_Preparation\create_model.ipynb` to create a SVM model for Iris Flower classification. Save the model as pickle file `iris_model.pkl`.
2. Copy the model file `iris_model.pkl` to folder `01_Server\model`.
3. In root folder, run command `python 01_Server\server.py` in terminal, API server will be hosted and watched at [http://localhost:5000](http://localhost:5000).
4. Open `02_Client\index.html` to launch the API Explorer.

![Screenshot](https://github.com/woo-chia-wei/flask-vue-iris/blob/master/assets/images/iris_api_explorer.png)
