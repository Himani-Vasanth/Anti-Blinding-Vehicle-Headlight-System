# Anti-Blinding-Vehicle-Headlight-System
A Python and Arduino-based project that detects approaching vehicles and controls an LED matrix to indicate their lane, helping to reduce headlight glare and improve road safety.

## Overview
The Anti-Blinding Headlight System is a project that combines Python and Arduino technologies to detect approaching vehicles and control an LED matrix to indicate their lane. This system helps reduce headlight glare, improving driving safety at night.

## Files
- **`python/car_detection.py`**: Python script that uses computer vision to detect vehicles and communicate lane information to the Arduino.
- **`python/haarcascade_car.xml`**: Haar cascade XML file used for vehicle detection.
- **`python/cars_video.mp4`**: Sample video file used for vehicle detection testing.
- **`arduino/AntiBlindingHeadlightSystem.ino`**: Arduino sketch that receives lane information and controls an LED matrix.

## Installation

### Python Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Himani-Vasanth/AntiBlindingHeadlightSystem.git

Navigate to the Python directory:
cd AntiBlindingHeadlightSystem/python

Install the required Python packages:
pip install opencv-python pyserial

Arduino Setup

    1. Open AntiBlindingHeadlightSystem.ino in the Arduino IDE.
    2. Connect your Arduino UNO to your computer.
    3. Select the correct board and port in the Arduino IDE.
    4. Upload the sketch to your Arduino.

Usage
    1. Run the Python Script:
    python car_detection.py
    Ensure the file paths in car_detection.py for haarcascade_car.xml and cars_video.mp4 are correctly set.

    2. Arduino:
    Make sure your Arduino is connected and running the uploaded sketch.

Configuration

    File Paths: Update the paths in the car_detection.py script to match the locations of the Haar cascade file and video file.
