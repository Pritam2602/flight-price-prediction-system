"""
Deployment script for Flight Price Prediction System
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    return True

def train_model():
    """Train the model if not exists"""
    if not os.path.exists("xgb_best.pkl"):
        print("Training model...")
        try:
            subprocess.check_call([sys.executable, "train_model.py"])
            print("✅ Model trained successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error training model: {e}")
            return False
    else:
        print("✅ Model already exists")
    return True

def run_application():
    """Run the Flask application"""
    print("Starting Flask application...")
    print("🌐 Application will be available at: http://localhost:5000")
    print("📱 Open your browser and navigate to the URL above")
    print("🛑 Press Ctrl+C to stop the application")
    
    try:
        subprocess.check_call([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running application: {e}")
        return False
    return True

def main():
    """Main deployment function"""
    print("🚀 Flight Price Prediction System - Deployment")
    print("=" * 50)
    
    # Install requirements
    if not install_requirements():
        return
    
    # Train model
    if not train_model():
        return
    
    # Run application
    run_application()

if __name__ == "__main__":
    main()
