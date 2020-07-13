import pickle
from flask import Flask,request,render_template
import pandas as pd
import numpy as np 
app = Flask(__name__)

load_model = pickle.load(open("cancer_dt_pkl","rb"))

cols = ['Age', 'Gender', 'Air Pollution', 'Alcohol use',
       'Dust Allergy', 'OccuPational Hazards', 'Genetic Risk',
       'chronic Lung Disease', 'Balanced Diet', 'Obesity', 'Smoking',
       'Passive Smoker', 'Chest Pain', 'Coughing of Blood']

@app.route("/")
def getmodel():
    return render_template("form.html")

@app.route("/prediction",methods=["POST"])
def predict():
    input_data = []
    
    for col in cols:
        input_data.append(int(request.form[col]))
        
    input_data = np.array(input_data)
    input_data = input_data.reshape(1,-1)
    print(input_data)
    
    pred = load_model.predict(input_data)
    
    if pred == 1:
        return "The severity of tumer is medium"
    elif pred == 0:
        return "The severity of tumer is low"
    elif pred == 2:
        return "The severity of tumer is high"
        
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)