import pickle
from flask import Flask,request,render_template,url_for
import numpy as np


model=pickle.load(open('loan.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('loanfirstpage.html')

@app.route('/predict',methods=['post'])
def predict():
     
    if request.method=='POST':
        gender=request.form['gender']
        if(gender=='male'):#1
           gender=1
        else:
            gender=0
            
        married=request.form['married']#yes-1
        if married=='yes':
            married=1
        else:
            married=0
            
        education=request.form['education']
        if education=='graduate':
            education=0
        else:
            education=1
        propertyarea=request.form['propertyarea']
        if propertyarea=='Semiurban':
            propertyarea=1
        elif propertyarea=='Rural':
            propertyarea=0
        else:
            propertyarea=2
        applicationincome=int(request.form['applicationincome'])
        coapplicantincome=int(request.form['coapplicantincome'])
        loanamount=int(request.form['loanamount'])
        loanamountterm=int(request.form['loanamountterm'])
        credithistory=int(request.form['credithistory'])
        
        
        prediction=model.predict([[gender,married,education,applicationincome,coapplicantincome,loanamount,loanamountterm,credithistory,propertyarea]])
        output=int(prediction)
        
        if output==1:
            return render_template('loanfirstpage.html',ans="Loan Granted ")
        else:
            return render_template('loanfirstpage.html',ans="Loan Not Granted")
            
        


if __name__=='__main__':
    app.run(debug=True)