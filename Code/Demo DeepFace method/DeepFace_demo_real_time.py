import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from keras.preprocessing import image
import warnings
warnings.filterwarnings("ignore")
from tensorflow.keras.preprocessing import image
from deepface import DeepFace

cap = cv2.VideoCapture(0)
# Check if the webcam is opened correctly
black = np.zeros((96,96))

face_haar_cascade = cv2.CascadeClassifier('E:\\Practice Introduction to Computer Vision\\EmotionalFaceRecognition_1\\haarcascade_frontalface_default.xml')
    
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(faceCascade.empty())
    faces_detected = face_haar_cascade.detectMultiScale(gray, 1.32, 5)
    
    # Draw a rectangle around the faces
    for(x, y, w, h) in faces_detected:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), thickness=4)

        roi_gray = gray[y:y+w, x:x+h]
        roi_gray = cv2.resize(roi_gray, (48,48))
        img_pixels = image.img_to_array(roi_gray)
        cv2.imshow('Gray img', roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
        img_pixels /= 255

        result = DeepFace.analyze(frame, actions = ['emotion'])
    
        cv2.putText(frame, result['dominant_emotion'], (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (219,68,55), 2)
    
    resized_img = cv2.resize(frame, (1000, 700))
    cv2.imshow('Original video', frame)
    
    if cv2.waitKey(10) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()