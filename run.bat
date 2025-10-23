@echo off
echo Flight Price Prediction System - Quick Start
echo ===========================================
echo.
echo Installing requirements...
pip install -r requirements.txt
echo.
echo Training model...
python train_model.py
echo.
echo Starting application...
echo Open your browser and go to: http://localhost:5000
echo Press Ctrl+C to stop the application
echo.
python app.py
pause
