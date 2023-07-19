import cv2
import easyocr
from collections import Counter
import requests


def verify_text(plate_number):
    # API endpoint URL
    url = 'http://localhost:5000/api/verify_text'

    # Number plate text to verify
    # number_plate = 'AAE 011'  # this one is dummy
    number_plate = plate_number  # this one is for real

    # Create the payload
    payload = {'text': number_plate}

    # Send the POST request to the API endpoint
    response = requests.post(url, json=payload)

    # Check the response
    if response.status_code == 200:
        data = response.json()
        exists = data.get('exists')
        print(exists)

        if exists:
            print(f"The number plate '{number_plate}' exists in the database.")
        else:
            print(
                f"The number plate '{number_plate}' does not exist in the database.")
    else:
        print("Error: Failed to receive a valid response from the API.")


# Path to the trained Haar cascade XML file for license plate detection
harcascade = "model/haarcascade_russian_plate_number.xml"

# Initialize video capture from default camera
cap = cv2.VideoCapture(0)

# Set the width and height of the video capture
cap.set(3, 640)  # width
cap.set(4, 480)  # height

# Minimum area threshold for license plate detection
min_area = 500

# Initialize a counter to track the number of detected plates
count = 0
recognized_texts = []

# Initialize EasyOCR reader with the desired language(s)
reader = easyocr.Reader(['en'])

while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # Load the license plate Haar cascade classifier
    plate_cascade = cv2.CascadeClassifier(harcascade)

    # Convert the frame to grayscale for license plate detection
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect license plates in the grayscale image
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    # Iterate over the detected license plates
    for (x, y, w, h) in plates:
        # Calculate the area of the license plate
        area = w * h

        # Check if the area exceeds the minimum area threshold
        if area > min_area:
            # Draw a rectangle around the license plate
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Extract the region of interest (ROI) containing the license plate
            img_roi = img[y: y+h, x:x+w]

            # Perform OCR on the ROI using EasyOCR
            results = reader.readtext(img_roi)

            # Extract the recognized text from the results
            text = [result[1] for result in results]
            verify_text(' '.join(text))

            # Print the recognized characters in the terminal
            print("License Plate:", ' '.join(text))

    # Display the resulting image with license plate detection
    cv2.imshow("Result", img)

    # Check if 's' key is pressed to save the detected license plate
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the image containing the license plate
        cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)

        # Display a confirmation message on the main image
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", img)

        # Wait for 500ms to display the confirmation message
        cv2.waitKey(500)

        # Increment the counter for the next detected license plate
        count += 1


# take help of the gate to count vehicle number
