import cv2
import numpy as np
import os
from keras.preprocessing import image
import warnings
warnings.filterwarnings("ignore")
from deepface import DeepFace

cap = cv2.VideoCapture(0)
# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    try:
        # Use DeepFace to detect faces and analyze emotions
        face_objs = DeepFace.extract_faces(img_path=frame, detector_backend='ssd', align=True)
        result = DeepFace.analyze(img_path=frame, actions=['emotion'], detector_backend='ssd', align=True)

        for face_obj in face_objs:
            x, y, w, h = face_obj['facial_area']['x'], face_obj['facial_area']['y'], face_obj['facial_area']['w'], face_obj['facial_area']['h']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=4)
            
            # Get emotion result for the current face
            dominant_emotion = result[0]['dominant_emotion']
            
            # Display the dominant emotion
            cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (219, 68, 55), 2)

    except Exception as e:
        # If no face is detected, just pass
        pass

    resized_img = cv2.resize(frame, (1000, 700))
    cv2.imshow('Original video', resized_img)
    
    if cv2.waitKey(10) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
