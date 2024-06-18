#!/bin/bash

# This script sets up the environment and runs the tests for the prompt-agent project

# Exit immediately if a command exits with a non-zero status
set -e

# Set up the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt
pip install pytest
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm
python -m spacy download fr_core_news_sm
python -m spacy download de_core_news_sm

# Run the tests
pytest --maxfail=1 --disable-warnings -q

# Deactivate the virtual environment
deactivate
