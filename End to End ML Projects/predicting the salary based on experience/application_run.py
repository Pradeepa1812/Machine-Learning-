import pickle
from flask import Flask,request,render_template
import pandas as pd
import numpy as np

app=Flask(__name__)
model=pickle.load(open('housepred.pkl','rb'))

@app.route('/')
def main():
     return render_template('main.html')


@app.route('/predict',methods=['POST'])
def predict():
    float_features=[float(x) for x in request.form.values()]
    final_features=[np.array(float_features)]
    prediction=np.round(model.predict(final_features))
    return render_template('main.html',prediction_text='Output will be Rs: {}'.format(float(prediction)))

if __name__=='__main__':
    app.run(debug=True)
