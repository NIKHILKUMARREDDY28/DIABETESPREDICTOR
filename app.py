import pandas as pd
#from app import app
import os 
import csv
from sklearn.model_selection import train_test_split
from flask import Flask,request,render_template,redirect,session, url_for
import pickle
app=Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('diabetes.html' )
@app.route('/template', methods=["GET", "POST"])
def template():
    data = []
    if request.method == 'POST':
        uploaded_file = request.files['csvfile'] # This line uses the same variable and worked fine
        if not os.path.isdir('static'):
            os.mkdir('static')
        filepath = os.path.join('static',uploaded_file.filename)
        uploaded_file.save(filepath)
        data = pd.read_csv(filepath)
        columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']
        data = data[columns]
        my_model = pickle.load(open("model.bin",'rb'))
        data['output']=my_model.predict(data)
    return render_template('template.html', tables=[data.to_html()], titles=[''])
if __name__ == "__main__":
    app.run(debug=True)    
