# 🚀 Flight Price Prediction System - Deployment Guide

## 📋 **Quick Start Options**

### **1. Local Development (Current)**
```bash
# Already running at http://localhost:5000
python app.py
```

### **2. Production Local Server**
```bash
# Windows
python run_production.py

# Linux/Mac
gunicorn --bind 0.0.0.0:8000 --workers 4 app:app
```

### **3. Docker Deployment**
```bash
# Build and run
docker build -t flight-prediction .
docker run -p 5000:5000 flight-prediction

# Or use docker-compose
docker-compose up -d
```

## 🌐 **Cloud Deployment Options**

### **🆓 FREE TIER OPTIONS**

#### **Heroku (Recommended for beginners)**
```bash
# Prerequisites: Install Heroku CLI
# 1. Create Heroku account
# 2. Install Heroku CLI
# 3. Run these commands:

heroku create your-app-name
git add .
git commit -m "Deploy flight prediction app"
git push heroku main
```

#### **Railway**
```bash
# Prerequisites: Install Railway CLI
railway login
railway init
railway up
```

#### **Render**
1. Go to [render.com](https://render.com)
2. Connect your GitHub repository
3. Set build command: `pip install -r requirements.txt && python train_model.py`
4. Set start command: `gunicorn --bind 0.0.0.0:$PORT app:app`
5. Deploy!

#### **Vercel**
```bash
# Install Vercel CLI
npm i -g vercel
vercel --prod
```

### **💰 PAID OPTIONS**

#### **AWS (Amazon Web Services)**
```bash
# Using Docker
docker build -t flight-prediction .
docker tag flight-prediction:latest your-account.dkr.ecr.region.amazonaws.com/flight-prediction:latest
docker push your-account.dkr.ecr.region.amazonaws.com/flight-prediction:latest

# Deploy to ECS, EKS, or EC2
```

#### **Google Cloud Platform**
```bash
# Using Cloud Run
gcloud run deploy flight-prediction --source . --platform managed --region us-central1
```

#### **Microsoft Azure**
```bash
# Using Azure Container Instances
az container create --resource-group myResourceGroup --name flight-prediction --image your-registry/flight-prediction
```

## 🛠 **Deployment Commands**

### **Quick Deploy Scripts**
```bash
# Windows - Production
python run_production.py

# Linux/Mac - Production
./run.sh

# Docker
docker-compose up -d

# Cloud deployment
python deploy_cloud.py
```

### **Manual Production Setup**
```bash
# Install production requirements
pip install -r requirements-prod.txt

# Train model
python train_model.py

# Run with Gunicorn (Linux/Mac)
gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 120 app:app

# Run with Waitress (Windows)
python -c "from waitress import serve; import app; serve(app.app, host='0.0.0.0', port=8000)"
```

## 🔧 **Environment Variables**

Create a `.env` file for production:
```env
FLASK_ENV=production
FLASK_DEBUG=False
PORT=5000
```

## 📊 **Performance Optimization**

### **For High Traffic**
```bash
# Use more workers
gunicorn --bind 0.0.0.0:8000 --workers 8 --timeout 120 app:app

# Use multiple processes
gunicorn --bind 0.0.0.0:8000 --workers 4 --worker-class gevent --worker-connections 1000 app:app
```

### **For Memory Optimization**
```bash
# Use fewer workers but more memory per worker
gunicorn --bind 0.0.0.0:8000 --workers 2 --max-requests 1000 --max-requests-jitter 100 app:app
```

## 🔒 **Security Considerations**

1. **Environment Variables**: Never commit API keys or secrets
2. **HTTPS**: Always use HTTPS in production
3. **CORS**: Configure CORS properly for your domain
4. **Rate Limiting**: Add rate limiting for API endpoints
5. **Input Validation**: Validate all user inputs

## 📈 **Monitoring & Logging**

### **Add Logging**
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In your app.py
logger.info(f"Prediction request: {data}")
```

### **Health Check Endpoint**
```python
@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'model_loaded': model is not None})
```

## 🚨 **Troubleshooting**

### **Common Issues**
1. **Port already in use**: Change port or kill existing process
2. **Model not found**: Run `python train_model.py` first
3. **Memory issues**: Reduce workers or increase server memory
4. **CORS errors**: Add CORS headers to your Flask app

### **Debug Commands**
```bash
# Check if app is running
curl http://localhost:5000/health

# Test prediction API
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"airline":"IndiGo","source":"Delhi","destination":"Mumbai","duration":"02:30","total_stops":1,"journey_day":15,"journey_month":12,"journey_year":2024,"dep_time":"14:30","arrival_time":"17:00"}'
```

## 📞 **Support**

If you encounter issues:
1. Check the logs: `docker logs <container_name>`
2. Test locally first: `python test_app.py`
3. Verify all dependencies: `pip list`
4. Check port availability: `netstat -tulpn | grep :5000`

## 🎯 **Recommended Deployment Path**

1. **Development**: Use `python app.py` (current)
2. **Testing**: Use `python run_production.py`
3. **Production**: Deploy to Heroku/Railway/Render
4. **Enterprise**: Use AWS/GCP/Azure with Docker

Your Flight Price Prediction System is ready for deployment! 🚀
