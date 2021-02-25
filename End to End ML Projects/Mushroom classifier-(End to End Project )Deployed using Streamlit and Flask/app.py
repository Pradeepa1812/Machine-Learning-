# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:25:30 2020

@author: Pradeepa
"""
import pickle
from flask import Flask,request,render_template,url_for
model=pickle.load(open('decisiontree.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('mmain.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        gill_color=int(request.form['gill-color'])
        ring_type=int(request.form['ring-type'])
        gill_size=int(request.form['gill-size'])
        bruises=int(request.form['bruises'])
        stalk_root=int(request.form['stalk-root'])
        gill_spacing=int(request.form['gill-spacing'])
        habitat=int(request.form['habitat'])
        spore_print_color=int(request.form['spore-print-color'])
        population=int(request.form['population'])
        prediction=model.predict([[gill_color,ring_type,gill_size,bruises,stalk_root,gill_spacing,habitat,spore_print_color,population]])
        return render_template('mmain.html',ans="The mushroom type is {}".format(int(prediction)))

if __name__=='__main__':
    app.run(debug=True)
    
    