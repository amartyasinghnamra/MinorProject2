# ANTRIX – Real-Time AI Emotion Detection System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.10-green)
![DeepFace](https://img.shields.io/badge/DeepFace-AI-orange)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19-red)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Overview

ANTRIX is a real-time AI-based emotion detection system built using Python, OpenCV, and DeepFace.  
The system captures live webcam frames, analyzes facial expressions using deep learning, and predicts dominant human emotions in real time.
ANTRIX is optimized for lightweight CPU-based execution and does not require dedicated GPU hardware.
The project is designed with:
- real-time responsiveness
- modular architecture
- beginner-friendly code structure
- safe error handling
- cross-platform compatibility
- reproducible setup process

This project was developed as part of a Minor Project for Bachelor of Technology in Artificial Intelligence and Machine Learning.

---

## Features

- Real-time webcam-based emotion detection
- AI-powered facial emotion analysis
- Dynamic resizable OpenCV window
- Safe application termination
- Beginner-friendly modular code structure
- Cross-platform webcam handling
- Lightweight CPU-based execution
- Clean UI overlay with live information

---

## Supported Emotions

ANTRIX can detect:
- Happy
- Sad
- Angry
- Fear
- Surprise
- Neutral
- Disgust

---

## Project Screenshot

<img width="819" height="447" alt="antrix-demo png" src="https://github.com/user-attachments/assets/2dd28801-b9ce-46e5-9671-0aa8245e150a" />

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| OpenCV | Webcam Capture & UI Rendering |
| DeepFace | Emotion Detection Engine |
| TensorFlow/Keras | Deep Learning Backend |
| NumPy | Frame/Data Processing |

---

# Project Structure

```bash
MinorProject2/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── main.py
│
├── Screenshots/
│   └── antrix-demo.png
```

---

# System Requirements

## Hardware Requirements

- Intel i3 / Ryzen 3 or higher
- Minimum 4 GB RAM
- Webcam (Built-in or USB)
- 500 MB free storage

---

## Software Requirements

- Python 3.12
- pip package manager
- Internet connection (first run only for model download)

---

# Installation Guide

## Step 1 — Clone Repository

```bash
git clone https://github.com/amartyasinghnamra/MinorProject2.git
```

---

## Step 2 — Open Project Folder

```bash
cd MinorProject2
```

---

## Step 3 — Create Virtual Environment (Recommended)

### Windows

```bash
python312 -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the application using:

```bash
python main.py
```
> Note: The first launch may take longer because DeepFace downloads pre-trained model weights automatically.
---

# Controls

| Key | Function |
|---|---|
| Q | Exit Application |
| Window Close Button | Safe Shutdown |

---

# How ANTRIX Works

1. Webcam initializes safely
2. Live frames are captured continuously
3. Frames are processed using DeepFace
4. Dominant emotion is detected
5. Emotion label is rendered on-screen
6. System loops in real time until exit

---

# Cross-Platform Support

ANTRIX supports:
- Windows 10/11
- Linux
- macOS

The webcam initialization automatically adapts based on the operating system.

---

# Troubleshooting

## Webcam Not Opening

Possible fixes:
- Close Zoom/Teams/Discord
- Check camera permissions
- Restart system
- Try changing CAMERA_INDEX value

---

## Slow First Launch

This is normal.

DeepFace downloads AI model weights during the first execution.

---

## TensorFlow Installation Issues

Upgrade pip before installation:

```bash
python -m pip install --upgrade pip
```

Then reinstall requirements.

---

## Black Screen / Empty Feed

Possible causes:
- Webcam already in use
- Invalid webcam index
- Camera permission denied

---

# Future Improvements

Potential future enhancements:
- Multi-face tracking
- Emotion history logging
- GUI interface using Tkinter/PyQt
- GPU acceleration
- Raspberry Pi deployment
- Mobile application integration
- Cloud synchronization

---

# Educational Purpose

This project was developed for:
- academic learning
- computer vision practice
- AI experimentation
- affective computing research

---

# Acknowledgements

- OpenCV
- DeepFace
- TensorFlow
- Python Community

---

# Author

Amartya Singh Namra

Bachelor of Technology  
Artificial Intelligence and Machine Learning

---

# License

This project is licensed under the MIT License.
