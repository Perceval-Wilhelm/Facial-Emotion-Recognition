import cv2
import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
from deepface import DeepFace

# Load model
trained_model = model_from_json(open("D:\\Projects\\Facial-Expression-Recognition\\Code\\CNN_from_scratch_method\\model\\best_face_model.json", "r").read())

# Load weights
trained_model.load_weights('D:\\Projects\\Facial-Expression-Recognition\\Code\\CNN_from_scratch_method\\model\\best_model.h5')

cap = cv2.VideoCapture(0)
emotions = ('angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise')

while True:
    ret, test_img = cap.read()

    if not ret:
        continue

    face_objs = DeepFace.extract_faces(img_path=test_img, detector_backend='opencv', align=True)

    for face_obj in face_objs:
        x, y, w, h = face_obj['facial_area']['x'], face_obj['facial_area']['y'], face_obj['facial_area']['w'], face_obj['facial_area']['h']
        face = face_obj['face']

        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=4)

        face = (face * 255).astype(np.uint8)
        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        face_gray = cv2.resize(face_gray, (48, 48))
        img_pixels = image.img_to_array(face_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        predictions = trained_model.predict(img_pixels)

        # Find max indexed array
        max_index = np.argmax(predictions[0])
        predicted_emotion = emotions[max_index]
        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (219, 68, 55), 2)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Predicted image', resized_img)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
