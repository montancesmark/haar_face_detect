# Real-Time Face Detection using OpenCV

![image](https://github.com/user-attachments/assets/8809c457-d10d-44c8-a959-a2a9dd4e912a)


This project demonstrates real-time face detection using OpenCV and Haar Cascade Classifiers, utilizing your webcam. The program captures video frames, applies basic image processing (such as grayscale conversion and binary thresholding), and detects faces in real-time. It then displays the original feed, grayscale feed, black-and-white feed, and a face-detection overlay.

## Features
- Real-time face detection with bounding boxes.
- Display of multiple video feeds (color, grayscale, black & white, face-detection).
- Simple controls for pausing and quitting the program.
- Uses Haar Cascade Classifier for face detection.

## Requirements

- Python 3.x
- OpenCV (`cv2`)

### Install dependencies

To run this project, you'll need Python and OpenCV installed on your system. You can install OpenCV using pip:

```bash
pip install opencv-python

```
## Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/montancesmark/haar_face_detect
```
Navigate into the project directory:
```bash
cd your_project_directory
```
Install the required dependencies (OpenCV):
```bash
pip install opencv-python
```
## Usage
Run the Python script to start the webcam and face detection:
```bash
python main.py
```
## The program will open a window with the following feeds:

Color Feed: The original webcam feed.
Grayscale Feed: A black and white version of the webcam feed.
Black and White Feed: The result of applying binary thresholding.
Face Detection: The original webcam feed with detected faces highlighted by green bounding boxes.
Press q to quit the program.

Press spacebar to pause the program. After pausing, press any key to resume.

## How it Works
The program:

Captures video from the webcam.
Converts each frame to grayscale.
Applies binary thresholding to create a black-and-white image.
Detects faces using the pre-trained Haar Cascade Classifier.
Draws bounding boxes around detected faces and displays the results in different windows.
Face Detection Algorithm
The face detection is powered by the Haar Cascade Classifier which is a machine learning-based method to detect objects in images. It is pre-trained on a dataset of human faces and can reliably detect frontal faces in a wide range of scenarios.



## Contributing
Fork this repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
OpenCV (https://opencv.org/) for providing the core library for computer vision tasks.
Haar Cascade Classifiers for face detection.
