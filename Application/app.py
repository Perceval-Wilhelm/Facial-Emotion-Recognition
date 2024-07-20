import streamlit as st
import numpy as np
import cv2
from keras.models import load_model
from deepface import DeepFace
from skimage.feature import hog
from sklearn import svm
from joblib import load
from PIL import Image

# Load pre-trained models
cnn_model = load_model('D:\\Projects\\Facial-Expression-Recognition\\Code\\CNN_from_scratch_method\\model\\best_model.h5')  # Path to your trained CNN model
svm_model = load('D:\\Projects\\Facial-Expression-Recognition\\Code\\SVM_method\\model\\svm_emotion_model.joblib')  # Path to your trained SVM model
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# Define paths for Haarcascade and DeepFace models
haarcascade_path = 'D:\\Projects\\Facial-Expression-Recognition\\Application\\haarcascade_frontalface_default.xml'  # Path to haarcascade
face_cascade = cv2.CascadeClassifier(haarcascade_path)

def extract_hog_features(image_array):
    if len(image_array.shape) == 3:  # Ensure image is 2D
        image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    hog_features, hog_image = hog(image_array, orientations=9, pixels_per_cell=(8, 8),
                                  cells_per_block=(2, 2), visualize=True)
    return hog_features

# Function to predict emotion using CNN model
def predict_emotion_cnn(image):
    face_objs = DeepFace.extract_faces(img_path=image, detector_backend='retinaface', align=True)
    if not face_objs:
        return "No face detected", []

    face = face_objs[0]['face']
    face = (face * 255).astype(np.uint8)
    img = cv2.resize(face, (48, 48))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img / 255.0
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)
    prediction = cnn_model.predict(img)
    emotion = emotion_dict[np.argmax(prediction)]
    return emotion, face_objs

# Function to predict emotion using SVM model
def predict_emotion_svm(image):
    img = cv2.resize(image, (48, 48))
    img = img / 255.0
    hog_features = extract_hog_features(img)
    hog_features = hog_features.reshape(1, -1)
    prediction = svm_model.predict(hog_features)
    emotion = prediction[0]
    return emotion

# Function to predict emotion using DeepFace
def predict_emotion_deepface(image):
    face_objs = DeepFace.extract_faces(img_path=image, detector_backend='retinaface', align=True)
    result = DeepFace.analyze(img_path=image, actions=['emotion'], detector_backend='retinaface', align=True)
    return face_objs, result[0]['dominant_emotion']

def draw_bounding_box(image, face_objs):
    for face_obj in face_objs:
        x, y, w, h = face_obj['facial_area']['x'], face_obj['facial_area']['y'], face_obj['facial_area']['w'], face_obj['facial_area']['h']
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image

def main():
    st.title("Emotion Detection Application")
    st.sidebar.title("Select Method")

    # Sidebar options
    method = st.sidebar.selectbox("Choose a method", ["CNN", "DeepFace", "SVM"])

    if "method" not in st.session_state or st.session_state.method != method:
        st.session_state.method = method
        st.experimental_rerun()

    # File uploader for image input
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = np.array(Image.open(uploaded_file))
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if method == "CNN":
            emotion, face_objs = predict_emotion_cnn(image)
        elif method == "DeepFace":
            face_objs, emotion = predict_emotion_deepface(image)
        elif method == "SVM":
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            face_objs = []
            for (x, y, w, h) in faces:
                face = gray[y:y+h, x:x+w]
                face = (face * 255).astype(np.uint8)  # Convert to uint8
                emotion = predict_emotion_svm(face)
                face_objs.append({'face': face, 'facial_area': {'x': x, 'y': y, 'w': w, 'h': h}})
                break  # Just take the first face found

        if face_objs:
            image_with_boxes = draw_bounding_box(image.copy(), face_objs)
            st.image(image_with_boxes, caption='Detected Face with Bounding Box', use_column_width=True)

        st.write(f"Predicted Emotion: {emotion}")

if __name__ == "__main__":
    main()
