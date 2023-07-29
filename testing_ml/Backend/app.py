# from flask import Flask, request, jsonify
# import numpy as np 
# import pickle
# from flask_cors import CORS
# import pandas as pd
# from sklearn.metrics import r2_score
# import json





# app = Flask(__name__)
# CORS(app)
# model_placement=pickle.load(open("placement.pkl","rb"))
# with open("data_file.json","rb") as json_file:
#     data=json.load(json_file)
#     accuracy=data
    



# # For the home route
# @app.route('/')
# def home():
#     response = {
#         'message': 'Welcome to the home route!'
#     }
#     return jsonify(response)

# # Predict route
# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     # Example: Extracting a specific value from the data
#     value1 = data.get('Cgpa')
    
#     # model lai chaiyea jastei requirement meet gareko
#     values = [float(value1)]
#     features=[np.array(values)]

#     # Model maa pathaalp

#     prediction=model_placement.predict(features)


  
    
#     # Aako data lai response maa pathaako 
#     # But this modal is always giving the same answer response
#     response = {
#        "prediction": prediction.tolist(),
#        "accuracy":accuracy
#     }

#     return jsonify(response)


# if __name__ == '__main__':
#     app.run(debug=True)












# the fuction for teh drop down menu
from flask import Flask, jsonify,json
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)






model=pickle.load(open("mlalgo.pkl","rb"))
with open("data_file.json","rb") as json_file:
    data=json.load(json_file)
    accuracy=data['model_accuracy']
    unique=data['unique_val']
    





@app.route('/api/options',methods=["POST"])
def get_dropdown_options():













    # Return the unique values as a response
    return jsonify({'unique_value':unique})

if __name__ == '__main__':
    app.run(debug=True)

