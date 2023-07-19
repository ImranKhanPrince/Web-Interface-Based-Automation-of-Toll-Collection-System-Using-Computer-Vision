# Project Title: Web Interface Based Automation of Toll Collection System Using Computer Vision

This is a repository for my BSC in EEE final Semester Project.

## **Introduction:**

This project aims to develop an automated toll collection system using computer
vision technology, web interface, and hardware integration. The system is
designed to enhance the efficiency and accuracy of toll collection, reducing
traffic congestion and human errors at toll plazas. This repository contains the
source code, computer vision model, and other relevant materials for the final
semester project of Bachelor of Science (BSc).

## **Project Overview:**

The toll collection system consists of three main modules: a camera and
detection module, a web server and verification module, and a hardware module.
The camera and detection module use Python and OpenCV to capture video, extract
the region of interest, and recognize license plate information using a Haar
Cascade classifier and EasyOCR library. The web server and verification module,
built with Flask, facilitate license plate verification and manage a database of
registered and passed cars. The hardware module, using an Arduino Uno, controls
the gate based on the verification status received from the web server.

## **Setup and Usage:**

To run the project, ensure you have Python and the required dependencies
installed. Use the following command to install the necessary packages:

```
pip install -r requirements.txt
```

Then, run the Python scripts for each module, ensuring that the camera is
properly connected to capture video for license plate recognition.

## **File Structure:**

```
|-- Arduino Hardware
|   |-- gateControl
|   |   |-- gateControl.ino
|-- Computer Vision Detector
|   |-- model
|   |   |-- haarcascade_russian_plate_number
|   |-- number-plate.py
|   |-- requirements.txt
|-- Web Server
|   |-- flask_app.py
|   |-- requirements.py
|   |-- templates
|   |   |-- index.html
```

## **Contributing:**

We welcome contributions to this project. If you find any issues or have ideas
for improvement, feel free to open an issue or submit a pull request. Let's
collaborate and make toll collection smarter and more efficient together!

## **License:**

This project is released under the [MIT License](LICENSE).

**Acknowledgments:** We would like to express our gratitude to our project
supervisor and mentors for their guidance and support throughout this project.
Special thanks to the OpenCV, EasyOCR, Flask, and Arduino communities for
providing invaluable tools and resources.

**Contact Information:** For any inquiries or questions, please contact us at
prince.imran.du@gmail.com.

Thank you for your interest in our BSc final semester project!
