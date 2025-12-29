#!/bin/bash

# Simple script to run the application

echo "Starting Doctor Appointment API..."
echo "Make sure you have:"
echo "1. Activated virtual environment (source venv/bin/activate)"
echo "2. Started database (docker-compose up -d)"
echo "3. Installed dependencies (pip install -r requirements.txt)"
echo ""
echo "Starting server..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

