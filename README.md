# Flight Price Prediction System

A modern web application that predicts flight prices using machine learning. Built with Flask backend and responsive HTML/CSS frontend.

## Features

- 🧠 **AI-Powered Predictions**: Uses XGBoost machine learning model
- ⚡ **Real-time Results**: Get instant price predictions
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- 🔒 **Reliable**: Based on extensive historical flight data

## Project Structure

```
flight_price_prediction_system/
├── app.py                 # Flask backend application
├── templates/
│   └── index.html        # Frontend HTML template
├── requirements.txt      # Python dependencies
├── Dockerfile          # Docker configuration
├── README.md           # This file
└── project_flight.ipynb # Original ML model training notebook
```

## Quick Start

### Option 1: Local Development

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Open in Browser**
   Navigate to `http://localhost:5000`

### Option 2: Docker Deployment

1. **Build Docker Image**
   ```bash
   docker build -t flight-price-prediction .
   ```

2. **Run Container**
   ```bash
   docker run -p 5000:5000 flight-price-prediction
   ```

3. **Access Application**
   Navigate to `http://localhost:5000`

## API Endpoints

- `GET /` - Main application page
- `POST /predict` - Get flight price prediction
- `GET /airlines` - Get list of available airlines
- `GET /destinations` - Get list of available destinations
- `GET /sources` - Get list of available source cities

## Prediction Input Format

```json
{
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
```

## Model Information

The system uses an XGBoost regressor trained on flight data with the following features:
- Airline (encoded)
- Source and Destination cities
- Flight duration
- Number of stops
- Journey date and time
- Departure and arrival times

## Deployment Options

### Heroku
1. Create a `Procfile` with: `web: python app.py`
2. Deploy using Heroku CLI

### AWS/GCP/Azure
- Use the provided Dockerfile
- Deploy to container services
- Configure load balancer for production

### Local Production
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Development

To extend the application:

1. **Add New Features**: Modify `app.py` and `templates/index.html`
2. **Update Model**: Retrain with new data and update model files
3. **Styling**: Modify CSS in the `<style>` section of `index.html`

## Requirements

- Python 3.7+
- Flask 2.3+
- Modern web browser
- Docker (optional)

## License

This project is open source and available under the MIT License.
