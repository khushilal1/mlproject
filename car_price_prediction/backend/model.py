from flask import Flask, render_template, request,jsonify
import numpy as np 
import pickle
from flask_cors import CORS
import pandas as pd
import json


app = Flask(__name__)
CORS(app)


#opening the file 
model = pickle.load(open('linear_regression.pkl', 'rb'))

#opening the val
with open("data_file.json","rb") as json_file:
    data=json.load(json_file)
    accuracy=data
    

# For the home route
@app.route('/')
def home():
    response = {
        'message': 'Welcome to the home route!'
    }
    return jsonify(response)









@app.route("/predict", methods=['POST','GET'])
def predict():

    data=request.get_json()
 #initializing the value of column of model
    Fuel_Type_Diesel=0
#getting the value of Year columns from frontend
    Year = int(data.get('Year'))
    Present_Price=float(data.get('Present_Price'))
    Kms_Driven=int(data.get('Kms_Driven'))
    Kms_Driven2=np.log(Kms_Driven)
    Owner=int(data.get('Owner'))
    Fuel_Type_Petrol=data.get('Fuel_Type_Petrol')
    if(Fuel_Type_Petrol=='Petrol' or  Fuel_Type_Petrol=="petrol"):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1

        #getting the number of year
    Year=2023-Year

    #making the data as 0 or 1
    Seller_Type_Individual=data.get('Seller_Type_Individual')
    if(Seller_Type_Individual=='Individual' or Seller_Type_Individual=='individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0	


    Transmission_Mannual=data.get('Transmission_Mannual')
    if(Transmission_Mannual=='mechanical' or Transmission_Mannual=='automatic'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0
        #predicting the value
    prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])

    #checking the value of the output
    output=round(prediction[0],2)
#    iving the same answer response
    response = {
       "prediction": output,
       "accuracy":accuracy
    }

    return jsonify(response)





if __name__=="__main__":
    app.run(debug=True)

