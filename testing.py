import cv2
import numpy as np

# recognizer = cv2.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('TrainingImageLabel/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

# Map IDs to names
id_to_name = {
    21: "Abhishek Singh",
    22: "Hima"
}

cam = cv2.VideoCapture(0)
while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
        
        # Get name from ID (default to "Unknown")
        name = id_to_name.get(Id, "Unknown")
        
        # Combine ID and name for display
        display_text = f"{name} ({Id})"

        # Draw rectangles and display text
        cv2.rectangle(im, (x, y), (x+w, y), (0, 255, 0), -1)  # Background for text
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 7)  # Face rectangle
        cv2.putText(im, display_text, (x, y-40), font, 1, (255, 255, 255), 2)
    else:
        id="Unknown"
    cv2.imshow('Processing.....', im)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
