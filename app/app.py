from flask import Flask, render_template, request, jsonify
import numpy as np
import os
from model import predict
#import seaborn as sns
#import matplotlib.pyplot as plt
#import pandas as pd

app = Flask(__name__)


UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png','jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST'])
def process_symptoms():
    try:
        symptoms = request.form['file1']
        # Assuming 'predict' is a function that takes symptoms as input and returns a prediction.
        prediction = predict(symptoms)
        return jsonify(result=prediction)
    except Exception as e:
        # It's a good practice to handle exceptions so that your app doesn't crash.
        # Respond with an error message or code.
        print(e)  # For debugging purposes; in production, consider logging.
        return jsonify(result="Error processing your request"), 500


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Assuming 'predict' function takes the symptom as input and returns a prediction
            symptoms = request.form['file1']
            result = predict(symptoms)
            return render_template('index.html', inp=symptoms, result=result)
        except Exception as e:
            # Log the error, inform the user something went wrong
            print(e)
            return render_template('index.html', inp="Error processing input", result="Could not process your request at this time.")
    else:
        # GET request, just render the initial form page
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)