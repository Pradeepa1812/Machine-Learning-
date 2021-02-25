import numpy as np
from flask import Flask,request,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  
    
    int_features=[float(x) for x in request.form.values()]
    final_feature=[np.array(int_features)]
    prediction=model.predict(final_feature)
    return render_template('index.html',prediction_text='Output of the turbine will be   {}  kW'.format(float(prediction)))




if __name__=='__main__':
    app.run(debug=True)