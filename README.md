
# Face Detection
## Overview
Face Detection is a simple Python application that utilizes computer vision to detect faces in real-time. The application is designed to trigger an alarm and produce a beep sound when a face moves towards the camera, and the distance between the face and the camera is less than 50cm.

## Features
Real-time face detection using computer vision.
Distance measurement between detected faces and the camera.
Audible alarm triggered when a face approaches within 50cm of the camera.

## Requirements
1. Python 3.x
2. OpenCV
3. Numpy
(Additional dependencies, if any, can be found in the requirements.txt file)

## Installation
Clone the repository:

``` bash
git clone https://github.com/SandaliKavi99/object_detection.git
 ```
Navigate to the project directory:

``` bash
cd object_detection
```
Install the required dependencies:

``` bash
pip install -r requirements.txt
```
## Usage
1. Run the application:

``` bash
python face_detection.py
```
2. Adjust the camera for optimal face detection.

3. When a face approaches within 50cm of the camera, the alarm will be triggered, and a beep sound will be produced.

## Configuration
You can modify the distance threshold and other parameters in the config.py file to suit your preferences.
Contributing
If you would like to contribute to this project, please follow the guidelines in the CONTRIBUTING.md file.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Special thanks to the contributors and the open-source community for their valuable contributions.
Feel free to explore, enhance, and contribute to the Face Detection project! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.


