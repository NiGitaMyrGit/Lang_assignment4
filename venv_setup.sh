#!/usr/bin/env bash

# Install venv on UCloud:
sudo apt-get update
sudo apt-get install python3-venv

# Create virtual environment
python3 -m venv spacy_env

# Activate virtual environment (only if running the script directly with Python)
source ./spacy_env/bin/activate

# Upgrade pip
python3 -m pip install --upgrade pip

# Install requirements
python3 -m pip install -r requirements.txt

# Run your Python script
python3 src/test.py