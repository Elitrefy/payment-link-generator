#!/bin/bash

# Update package lists
apt-get update

# Install required system dependencies
apt-get install -y libgl1-mesa-glx libglib2.0-0 google-chrome-stable

# Install Python dependencies
pip install -r requirements.txt
