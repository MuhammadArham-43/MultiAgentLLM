#!/bin/bash
VENV_DIR="venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating a new virutal environment venv for Python"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else source venv/bin/activate
fi
nohup ollama serve &
set -a
source .env
nohup streamlit run client.py &
python3 main.py