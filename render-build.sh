#!/bin/bash

# Update package lists
apt-get update

# Install required system dependencies for Kivy
apt-get install -y libgl1-mesa-glx libglib2.0-0 \
                   python3-setuptools python3-pip python3-dev \
                   python3-virtualenv libgles2-mesa libgles2-mesa-dev \
                   libmtdev1 libx11-dev libxcursor-dev libxrandr-dev \
                   libxi-dev libxss-dev x11-utils mesa-utils xvfb \
                   ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
                   libsdl2-ttf-dev libportmidi-dev libswscale-dev \
                   libavformat-dev libavcodec-dev zlib1g-dev

# Install Python dependencies
pip install --upgrade pip  # Ensure latest pip
pip install -r requirements.txt
