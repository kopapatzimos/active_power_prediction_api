from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Load model 
rf_model = joblib.load('random_forest_model.joblib')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json(force=True)
    
    # Convert data into DataFrame format
    input_data = pd.DataFrame([data])

    # Make predictions
    predictions = rf_model.predict(input_data)
    
    # Return predictions as JSON
    return jsonify({'Predicted Active Power for your Inputs': f"{predictions[0]:.2f}"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
