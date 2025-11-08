#!/bin/bash
# start_server.command - for macOS
# Usage: double-click this file in Finder, or run in terminal: ./start_server.command
SETUP_FLAG=".venv_created"
if [ ! -f "$SETUP_FLAG" ]; then
  echo "Creating virtual environment and installing dependencies..."
  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  touch "$SETUP_FLAG"
  echo "Setup complete."
fi
echo "Starting server... (Press Ctrl+C to stop)"
source venv/bin/activate
# Run Flask app
python3 flask_app.py
