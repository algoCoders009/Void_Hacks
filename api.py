from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib
from flask_cors import CORS, cross_origin
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)
cors = CORS(app, resources={r"/predict": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))
	    pred=jsonify({'prediction': str(prediction)})

            return pred

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    lr = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)
