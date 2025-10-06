#!/bin/bash

# Solar Station Application Deployment Script
# Usage: sudo ./deploy.sh

set -e

echo "🚀 Starting deployment..."

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}Please run as root (use sudo)${NC}"
    exit 1
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Docker installation
if ! command_exists docker; then
    echo -e "${RED}Docker is not installed. Installing...${NC}"
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    rm get-docker.sh
fi

# Check Docker Compose installation
if ! command_exists docker-compose; then
    echo -e "${YELLOW}Docker Compose is not installed. Installing...${NC}"
    curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
fi

echo -e "${GREEN}✓ Docker and Docker Compose are ready${NC}"

# Stop existing containers
echo -e "${YELLOW}Stopping existing containers...${NC}"
docker-compose down 2>/dev/null || true

# Build and start containers
echo -e "${GREEN}Building and starting containers...${NC}"
docker-compose up -d --build

# Wait for services to be ready
echo -e "${YELLOW}Waiting for services to start...${NC}"
sleep 5

# Check container status
if docker-compose ps | grep -q "Up"; then
    echo -e "${GREEN}✓ Deployment successful!${NC}"
    echo ""
    echo "Container status:"
    docker-compose ps
    echo ""
    echo -e "${GREEN}Application is running at: http://$(hostname -I | awk '{print $1}'):5000${NC}"
    echo ""
    echo "Useful commands:"
    echo "  View logs:     sudo docker-compose logs -f"
    echo "  Stop:          sudo docker-compose down"
    echo "  Restart:       sudo docker-compose restart"
else
    echo -e "${RED}✗ Deployment failed. Check logs:${NC}"
    docker-compose logs
    exit 1
fi

