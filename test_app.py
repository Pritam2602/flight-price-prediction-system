"""
Test script for the Flight Price Prediction API
"""

import requests
import json

def test_api():
    """Test the API endpoints"""
    base_url = "http://localhost:5000"
    
    print("Testing Flight Price Prediction API...")
    
    # Test airlines endpoint
    try:
        response = requests.get(f"{base_url}/airlines")
        if response.status_code == 200:
            airlines = response.json()
            print(f"[OK] Airlines endpoint working. Found {len(airlines)} airlines")
        else:
            print(f"[ERROR] Airlines endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Airlines endpoint error: {e}")
    
    # Test sources endpoint
    try:
        response = requests.get(f"{base_url}/sources")
        if response.status_code == 200:
            sources = response.json()
            print(f"[OK] Sources endpoint working. Found {len(sources)} sources")
        else:
            print(f"[ERROR] Sources endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Sources endpoint error: {e}")
    
    # Test destinations endpoint
    try:
        response = requests.get(f"{base_url}/destinations")
        if response.status_code == 200:
            destinations = response.json()
            print(f"[OK] Destinations endpoint working. Found {len(destinations)} destinations")
        else:
            print(f"[ERROR] Destinations endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Destinations endpoint error: {e}")
    
    # Test prediction endpoint
    test_data = {
        "airline": "IndiGo",
        "source": "Delhi",
        "destination": "Mumbai",
        "duration": "02:30",
        "total_stops": 1,
        "journey_day": 15,
        "journey_month": 12,
        "journey_year": 2024,
        "dep_time": "14:30",
        "arrival_time": "17:00"
    }
    
    try:
        response = requests.post(f"{base_url}/predict", 
                               json=test_data,
                               headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            result = response.json()
            print(f"[OK] Prediction endpoint working. Predicted price: Rs.{result['predicted_price']}")
        else:
            print(f"[ERROR] Prediction endpoint failed: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"[ERROR] Prediction endpoint error: {e}")
    
    print("\n[SUCCESS] API testing completed!")

if __name__ == "__main__":
    test_api()
