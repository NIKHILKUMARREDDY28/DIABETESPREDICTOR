import pandas as pd
from sklearn.model_selection import train_test_split
from flask import Flask,request,render_template
import pickle
app=Flask(__name__)

@app.route('/')
def home():
    
    return render_template('diabetes.html')
@app.route('/template',methods=['POST'])
def template():
    print(type(request.form.get("csvfile")))
    data = pd.read_csv("diabetes.csv")
    X = data.drop(["Outcome"], axis=1)
    y = data["Outcome"]
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=100)
        
    model=pickle.load(open("model.bin",'rb'))
    outp = model.predict(X) 
    data["predicted"] = outp
    data.to_excel("output.xlsx")
    return render_template("template.html")
if __name__ == "__main__":
    app.run(debug=True)    
