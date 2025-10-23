"""
Model training script for Flight Price Prediction System
This script recreates the XGBoost model from the original notebook
"""

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

def create_sample_data():
    """Create sample flight data for demonstration"""
    np.random.seed(42)
    n_samples = 1000
    
    # Sample data based on the original dataset structure
    airlines = ['Trujet', 'SpiceJet', 'Air Asia', 'IndiGo', 'GoAir', 'Vistara', 
                'Vistara Premium economy', 'Air India', 'Multiple carriers', 
                'Multiple carriers Premium economy', 'Jet Airways', 'Jet Airways Business']
    
    sources = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']
    destinations = ['Kolkata', 'Hyderabad', 'Delhi', 'Banglore', 'Cochin', 'New Delhi']
    
    data = {
        'Airline': np.random.choice(airlines, n_samples),
        'Source': np.random.choice(sources, n_samples),
        'Destination': np.random.choice(destinations, n_samples),
        'Duration': np.random.randint(60, 600, n_samples),  # minutes
        'Total_Stops': np.random.choice([0, 1, 2, 3, 4], n_samples),
        'Journey_day': np.random.randint(1, 32, n_samples),
        'Journey_month': np.random.randint(1, 13, n_samples),
        'Journey_year': np.random.choice([2019, 2020, 2021, 2022, 2023, 2024], n_samples),
        'Dep_Time_hour': np.random.randint(0, 24, n_samples),
        'Dep_Time_minute': np.random.randint(0, 60, n_samples),
        'Arrival_Time_hour': np.random.randint(0, 24, n_samples),
        'Arrival_Time_minute': np.random.randint(0, 60, n_samples),
        'Duration_hour': np.random.randint(1, 12, n_samples),
        'Duration_minute': np.random.randint(0, 60, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Create source dummy variables
    for source in sources:
        df[f'Source_{source}'] = (df['Source'] == source).astype(int)
    
    # Create price based on features (simplified pricing model)
    base_price = 3000
    airline_multiplier = df['Airline'].map({airline: idx * 200 for idx, airline in enumerate(airlines)})
    destination_multiplier = df['Destination'].map({dest: idx * 300 for idx, dest in enumerate(destinations)})
    duration_multiplier = df['Duration'] * 2
    stops_multiplier = df['Total_Stops'] * 500
    time_multiplier = df['Dep_Time_hour'] * 50
    
    df['Price'] = (base_price + airline_multiplier + destination_multiplier + 
                   duration_multiplier + stops_multiplier + time_multiplier + 
                   np.random.normal(0, 1000, n_samples)).astype(int)
    
    return df

def preprocess_data(df):
    """Preprocess the data for training"""
    # Create encoders
    airlines = df.groupby(['Airline'])['Price'].mean().sort_values().index
    dict_air = {key: idx for idx, key in enumerate(airlines, 0)}
    
    destinations = df.groupby(['Destination'])['Price'].mean().sort_values().index
    dict_des = {key: idx for idx, key in enumerate(destinations, 0)}
    
    dict_stp = {'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4}
    
    # Encode categorical variables
    df['Airline'] = df['Airline'].map(dict_air)
    df['Destination'] = df['Destination'].map(dict_des)
    df['Total_Stops'] = df['Total_Stops'].map(dict_stp)
    
    # Prepare features and target
    X = df.drop(['Source', 'Price'], axis=1)
    y = df['Price']
    
    return X, y, dict_air, dict_des, dict_stp

def train_model():
    """Train the XGBoost model"""
    print("Creating sample data...")
    df = create_sample_data()
    
    print("Preprocessing data...")
    X, y, dict_air, dict_des, dict_stp = preprocess_data(df)
    
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training XGBoost model...")
    # XGBoost parameters (simplified for demonstration)
    model = xgb.XGBRegressor(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Performance:")
    print(f"RMSE: {np.sqrt(mse):.2f}")
    print(f"R² Score: {r2:.4f}")
    
    print("Saving model and encoders...")
    joblib.dump(model, "xgb_best.pkl")
    joblib.dump(dict_air, "dict_air.pkl")
    joblib.dump(dict_des, "dict_des.pkl")
    joblib.dump(dict_stp, "dict_stp.pkl")
    
    print("Model training completed successfully!")
    print(f"Saved files: xgb_best.pkl, dict_air.pkl, dict_des.pkl, dict_stp.pkl")

if __name__ == "__main__":
    train_model()
