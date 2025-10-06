#!/bin/bash

# Continuous Deployment Script for Solar Energy Management API
# This script automates deployment to AWS EC2

set -e  # Exit on any error

echo "🚀 Starting deployment to AWS EC2..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
SERVER_IP="54.198.153.234"
SERVER_USER="admin"
APP_PATH="/home/admin/database_labs"
SSH_KEY_PATH="~/Downloads/yuliana key.pem"

echo -e "${YELLOW}📡 Connecting to server $SERVER_IP...${NC}"

# Deploy to server
ssh -i $SSH_KEY_PATH $SERVER_USER@$SERVER_IP << 'EOF'
set -e

echo "📂 Navigating to application directory..."
cd /home/admin/database_labs

echo "⬇️  Pulling latest changes from GitHub..."
git pull origin lab4

echo "🐳 Stopping existing containers..."
cd mybd
sudo docker-compose down

echo "🔨 Building new Docker image..."
sudo docker-compose build --no-cache

echo "🚀 Starting application..."
sudo docker-compose up -d

echo "⏳ Waiting for application to start..."
sleep 20

echo "✅ Deployment completed!"
EOF

echo -e "${YELLOW}🔍 Running health checks...${NC}"

# Health check
sleep 10
response=$(curl -s -o /dev/null -w "%{http_code}" http://$SERVER_IP:5000/)

if [ $response -eq 200 ]; then
    echo -e "${GREEN}✅ Deployment successful!${NC}"
    echo -e "${GREEN}🌐 Application URL: http://$SERVER_IP:5000/${NC}"
    echo -e "${GREEN}📚 Swagger UI: http://$SERVER_IP:5000/swagger/${NC}"
    echo -e "${GREEN}🎉 Solar Energy Management API is now live!${NC}"
else
    echo -e "${RED}❌ Health check failed with status code: $response${NC}"
    echo -e "${RED}Please check the application logs.${NC}"
    exit 1
fi
