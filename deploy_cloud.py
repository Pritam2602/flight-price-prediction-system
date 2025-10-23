"""
Cloud deployment script for Flight Price Prediction System
Supports: Heroku, Railway, Render, AWS, GCP, Azure
"""

import subprocess
import sys
import os

def deploy_heroku():
    """Deploy to Heroku"""
    print("🚀 Deploying to Heroku...")
    print("Make sure you have Heroku CLI installed and are logged in")
    
    commands = [
        "heroku create flight-price-prediction",
        "git add .",
        "git commit -m 'Deploy flight price prediction app'",
        "git push heroku main"
    ]
    
    for cmd in commands:
        print(f"Running: {cmd}")
        try:
            subprocess.check_call(cmd.split())
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: {e}")
            return False
    
    print("✅ Deployed to Heroku!")
    print("🌐 Your app will be available at: https://flight-price-prediction.herokuapp.com")
    return True

def deploy_railway():
    """Deploy to Railway"""
    print("🚀 Deploying to Railway...")
    print("Make sure you have Railway CLI installed and are logged in")
    
    commands = [
        "railway login",
        "railway init",
        "railway up"
    ]
    
    for cmd in commands:
        print(f"Running: {cmd}")
        try:
            subprocess.check_call(cmd.split())
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: {e}")
            return False
    
    print("✅ Deployed to Railway!")
    return True

def deploy_render():
    """Deploy to Render"""
    print("🚀 Deploying to Render...")
    print("1. Go to https://render.com")
    print("2. Connect your GitHub repository")
    print("3. Set build command: pip install -r requirements.txt && python train_model.py")
    print("4. Set start command: gunicorn --bind 0.0.0.0:$PORT app:app")
    print("5. Deploy!")
    
    return True

def deploy_aws():
    """Deploy to AWS"""
    print("🚀 Deploying to AWS...")
    print("Using Docker deployment...")
    
    commands = [
        "docker build -t flight-prediction .",
        "docker tag flight-prediction:latest your-account.dkr.ecr.region.amazonaws.com/flight-prediction:latest",
        "docker push your-account.dkr.ecr.region.amazonaws.com/flight-prediction:latest"
    ]
    
    print("Docker commands to run:")
    for cmd in commands:
        print(f"  {cmd}")
    
    print("\nThen deploy to ECS, EKS, or EC2")
    return True

def main():
    """Main deployment function"""
    print("🌐 Flight Price Prediction System - Cloud Deployment")
    print("=" * 60)
    print("Choose your deployment platform:")
    print("1. Heroku (Free tier available)")
    print("2. Railway (Free tier available)")
    print("3. Render (Free tier available)")
    print("4. AWS (Pay as you go)")
    print("5. Show all options")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        deploy_heroku()
    elif choice == "2":
        deploy_railway()
    elif choice == "3":
        deploy_render()
    elif choice == "4":
        deploy_aws()
    elif choice == "5":
        print("\n📋 All Deployment Options:")
        print("=" * 40)
        print("🆓 FREE TIER OPTIONS:")
        print("• Heroku: https://heroku.com")
        print("• Railway: https://railway.app")
        print("• Render: https://render.com")
        print("• Vercel: https://vercel.com")
        print("• Netlify: https://netlify.com")
        print("\n💰 PAID OPTIONS:")
        print("• AWS: https://aws.amazon.com")
        print("• Google Cloud: https://cloud.google.com")
        print("• Azure: https://azure.microsoft.com")
        print("• DigitalOcean: https://digitalocean.com")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
