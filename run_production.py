"""
Production deployment script for Flight Price Prediction System
"""

import subprocess
import sys
import os

def install_production_requirements():
    """Install production requirements"""
    print("Installing production requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements-prod.txt"])
        print("✅ Production requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing production requirements: {e}")
        return False
    return True

def run_with_gunicorn():
    """Run with Gunicorn (Linux/Mac)"""
    print("🚀 Starting production server with Gunicorn...")
    print("🌐 Application will be available at: http://localhost:8000")
    print("🛑 Press Ctrl+C to stop the application")
    
    try:
        subprocess.check_call([
            "gunicorn", 
            "--bind", "0.0.0.0:8000",
            "--workers", "4",
            "--timeout", "120",
            "app:app"
        ])
    except KeyboardInterrupt:
        print("\n👋 Production server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Gunicorn: {e}")
        return False
    return True

def run_with_waitress():
    """Run with Waitress (Windows/Linux/Mac)"""
    print("🚀 Starting production server with Waitress...")
    print("🌐 Application will be available at: http://localhost:8000")
    print("🛑 Press Ctrl+C to stop the application")
    
    try:
        from waitress import serve
        import app
        serve(app.app, host="0.0.0.0", port=8000)
    except KeyboardInterrupt:
        print("\n👋 Production server stopped by user")
    except Exception as e:
        print(f"❌ Error running Waitress: {e}")
        return False
    return True

def main():
    """Main production deployment function"""
    print("🚀 Flight Price Prediction System - Production Deployment")
    print("=" * 60)
    
    # Install production requirements
    if not install_production_requirements():
        return
    
    # Choose server based on OS
    import platform
    system = platform.system().lower()
    
    if system == "windows":
        print("🪟 Windows detected - using Waitress server")
        run_with_waitress()
    else:
        print("🐧 Unix/Linux detected - using Gunicorn server")
        run_with_gunicorn()

if __name__ == "__main__":
    main()
