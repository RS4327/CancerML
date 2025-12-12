
from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from CancerML.Pipeline.predict_pipeline import custom_data,ModelPreidctPipeline

application =Flask(__name__)
app=application
##Route for a home page

@app.route("/")
def indx():
    return render_template('index.html')


#@app.route('/predictdata',method=['GET','POST'])
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else :
        print("Received form fields:", request.form)
        data=custom_data(

            lcavol =request.form.get('lcavol'),
            lweight=request.form.get('lweight'),
            age	   =request.form.get('age'),
            lbph	=request.form.get('lbph'),
            svi	   =request.form.get('svi'),
            lcp	   =request.form.get('lcp'),
            gleason=request.form.get('gleason'),
            pgg45	=request.form.get('pgg45'),
            lpsa	=request.form.get('lpsa'),
            train	=request.form.get('train'),

        )
        pred_df=data.get_data_as_frame_data()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=ModelPreidctPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)[0]#  this returns 0 or 1
        print("after Prediction")
        label = "a fraudulent" if results == 1 else "not a fraudulent"
        return render_template('home.html',results=label)


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)