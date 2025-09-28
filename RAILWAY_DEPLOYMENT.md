# Railway Deployment Guide

## 🚀 Quick Setup

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Railway deployment"
   git push origin main
   ```

2. **Connect to Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository

3. **Configure Environment Variables**
   In Railway dashboard, add these variables:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.railway.app
   RAILWAY_ENVIRONMENT=production
   ```

4. **Add PostgreSQL Database**
   - In Railway dashboard, click "New" → "Database" → "PostgreSQL"
   - Railway will automatically set DATABASE_URL

## 📁 File Storage

- **Development**: Images stored in `media/` directory
- **Production**: Images stored in `storage/` directory (Railway persistent volume)
- **Upload via**: Django Admin → Site Settings

## 🔧 Configuration Files Created

- `requirements.txt` - Python dependencies
- `Procfile` - Railway startup command
- `railway.json` - Railway configuration
- `storage/` - Production media directory

## 🌐 After Deployment

Your portfolio will be available at:
`https://your-app-name.railway.app`

Images will be accessible at:
`https://your-app-name.railway.app/media/backgrounds/your-image.jpg`
