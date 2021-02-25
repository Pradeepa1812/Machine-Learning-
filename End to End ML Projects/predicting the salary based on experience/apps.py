from flask import Flask,render_template,request
import numpy as np
import pickle
app=Flask(__name__)
model=pickle.load(open('salary.pkl','rb'))

@app.route('/')

def mains():
    return render_template('salary_main.html')

@app.route('/predict' ,methods=['POST'])
def predict():
       Experience=float(request.form['Experience'])
       predictions=model.predict([[Experience]])
       return render_template('salary_main.html',predict_value="The Salary is {:}".format(float(predictions)))



if __name__=='__main__':
    app.run(debug=True)