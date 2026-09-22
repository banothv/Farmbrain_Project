import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model("farmbrain_model.h5")

IMG_SIZE = 128

def predict_image(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.reshape(img, (1, IMG_SIZE, IMG_SIZE, 3))

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        print("Diseased Plant")
    else:
        print("Healthy Plant")

predict_image("test.jpg")
