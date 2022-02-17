from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np
from PIL import Image

import joblib
app = Flask(__name__)



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/diabetes", methods=['GET', 'POST'])
def diabetesPage():
    return render_template('diabetes.html')

@app.route("/cancer", methods=['GET', 'POST'])
def cancerPage():
    return render_template('breast_cancer.html')

@app.route("/heart", methods=['GET', 'POST'])
def heartPage():
    return render_template('heart.html')

@app.route("/kidney", methods=['GET', 'POST'])
def kidneyPage():
    return render_template('kidney.html')

@app.route("/liver", methods=['GET', 'POST'])
def liverPage():
    return render_template('liver.html')

@app.route("/malaria", methods=['GET', 'POST'])
def malariaPage():
    return render_template('malaria.html')

@app.route("/pneumonia", methods=['GET', 'POST'])
def pneumoniaPage():
    return render_template('pneumonia.html')


def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==8):#Diabetes
        loaded_model = joblib.load("diabetes")
        result = loaded_model.predict(to_predict)
    elif(size==26):#Cancer
        loaded_model = joblib.load("breast_cancer")
        result = loaded_model.predict(to_predict)
    elif(size==18):#Kidney
        loaded_model = joblib.load("kidney")
        result = loaded_model.predict(to_predict)
    elif(size==10):
        loaded_model = joblib.load("liver")
        result = loaded_model.predict(to_predict)
    elif(size==13):#Heart
        loaded_model = joblib.load("heart")
        result =loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict',methods = ["POST"])
def predictPage():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==26):#Cancer
            result = ValuePredictor(to_predict_list,26)
        elif(len(to_predict_list)==8):#Daiabtes
            result = ValuePredictor(to_predict_list,8)
        elif(len(to_predict_list)==18):
            result = ValuePredictor(to_predict_list,18)
        elif(len(to_predict_list)==13):
            result = ValuePredictor(to_predict_list,13)
            #if int(result)==1:
            #   prediction ='diabetes'
            #else:
            #   prediction='Healthy' 
        elif(len(to_predict_list)==10):
            result = ValuePredictor(to_predict_list,10)
    if(int(result)==1):
        prediction='Sorry ! Suffering'
    else:
        prediction='Congrats ! you are Healthy' 
    return(render_template("predict.html", pred=prediction))


if __name__ == '__main__':
	app.run(debug = True)