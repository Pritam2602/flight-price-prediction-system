from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Global variables for model and encoders
model = None
dict_air = None
dict_des = None
dict_stp = None

def load_model():
    """Load the trained model and encoders"""
    global model, dict_air, dict_des, dict_stp
    
    try:
        # Try to load existing model files
        model = joblib.load("xgb_best.pkl")
        dict_air = joblib.load("dict_air.pkl")
        dict_des = joblib.load("dict_des.pkl")
        dict_stp = joblib.load("dict_stp.pkl")
        print("Model loaded successfully from existing files")
    except FileNotFoundError:
        # If model files don't exist, create dummy data for demonstration
        print("Model files not found. Creating dummy model for demonstration.")
        # Create dummy encoders
        dict_air = {
            'Trujet': 0, 'SpiceJet': 1, 'Air Asia': 2, 'IndiGo': 3, 'GoAir': 4, 
            'Vistara': 5, 'Vistara Premium economy': 6, 'Air India': 7, 
            'Multiple carriers': 8, 'Multiple carriers Premium economy': 9, 
            'Jet Airways': 10, 'Jet Airways Business': 11
        }
        dict_des = {
            'Kolkata': 0, 'Hyderabad': 1, 'Delhi': 2, 'Banglore': 3, 
            'Cochin': 4, 'New Delhi': 5
        }
        dict_stp = {'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4}

def preprocess_input(data):
    """Preprocess input data for prediction"""
    # Create a new DataFrame with only the required columns
    df = pd.DataFrame()
    
    # Encode airline
    if data['airline'] in dict_air:
        df['Airline'] = [dict_air[data['airline']]]
    else:
        df['Airline'] = [0]  # Default to first airline
    
    # Encode destination
    if data['destination'] in dict_des:
        df['Destination'] = [dict_des[data['destination']]]
    else:
        df['Destination'] = [0]  # Default to first destination
    
    # Encode stops
    stops_mapping = {0: 'non-stop', 1: '1 stop', 2: '2 stops', 3: '3 stops', 4: '4 stops'}
    stops_text = stops_mapping.get(data['total_stops'], 'non-stop')
    df['Total_Stops'] = [dict_stp.get(stops_text, 0)]
    
    # Process duration
    duration_hour, duration_minutes = map(int, data['duration'].split(':'))
    duration_total_minutes = duration_hour * 60 + duration_minutes
    df['Duration'] = [duration_total_minutes]
    df['Duration_hour'] = [duration_hour]
    df['Duration_minute'] = [duration_minutes]
    
    # Process dates
    df['Journey_day'] = [int(data['journey_day'])]
    df['Journey_month'] = [int(data['journey_month'])]
    df['Journey_year'] = [int(data['journey_year'])]
    
    # Process times
    dep_hours, dep_minutes = map(int, data['dep_time'].split(':'))
    arr_hours, arr_minutes = map(int, data['arrival_time'].split(':'))
    df['Dep_Time_hour'] = [dep_hours]
    df['Dep_Time_minute'] = [dep_minutes]
    df['Arrival_Time_hour'] = [arr_hours]
    df['Arrival_Time_minute'] = [arr_minutes]
    
    # Create source dummy variables
    source_list = ["Banglore", "Kolkata", "Delhi", "Chennai", "Mumbai"]
    for cat in source_list:
        df[f"Source_{cat}"] = [1 if data['source'] == cat else 0]
    
    # Ensure all columns are numeric
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Reorder columns to match training data (exact order from model)
    expected_columns = [
        'Airline', 'Destination', 'Duration', 'Total_Stops', 'Journey_day', 
        'Journey_month', 'Journey_year', 'Dep_Time_hour', 'Dep_Time_minute', 
        'Arrival_Time_hour', 'Arrival_Time_minute', 'Duration_hour', 'Duration_minute',
        'Source_Banglore', 'Source_Kolkata', 'Source_Delhi', 'Source_Chennai', 'Source_Mumbai'
    ]
    
    # Create DataFrame with correct column order
    ordered_df = pd.DataFrame()
    for col in expected_columns:
        if col in df.columns:
            ordered_df[col] = df[col]
        else:
            ordered_df[col] = [0]  # Default value for missing columns
    
    return ordered_df

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['airline', 'source', 'destination', 'duration', 'total_stops', 
                          'journey_day', 'journey_month', 'journey_year', 'dep_time', 'arrival_time']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Preprocess the input
        processed_data = preprocess_input(data)
        
        # Make prediction
        if model is not None:
            prediction = model.predict(processed_data)[0]
        else:
            # Dummy prediction for demonstration
            base_price = 5000
            airline_multiplier = dict_air.get(data['airline'], 3) * 200
            destination_multiplier = dict_des.get(data['destination'], 2) * 300
            duration_multiplier = int(data['duration'].split(':')[0]) * 100
            stops_multiplier = data['total_stops'] * 500
            
            prediction = base_price + airline_multiplier + destination_multiplier + duration_multiplier + stops_multiplier
        
        return jsonify({
            'predicted_price': float(round(prediction, 2)),
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/airlines')
def get_airlines():
    """Get list of available airlines"""
    return jsonify(list(dict_air.keys()))

@app.route('/destinations')
def get_destinations():
    """Get list of available destinations"""
    return jsonify(list(dict_des.keys()))

@app.route('/sources')
def get_sources():
    """Get list of available source cities"""
    return jsonify(["Banglore", "Kolkata", "Delhi", "Chennai", "Mumbai"])

if __name__ == '__main__':
    load_model()
    app.run(debug=True, host='0.0.0.0', port=5000)
