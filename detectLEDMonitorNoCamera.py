# from keras.models import load_model  # TensorFlow is required for Keras to work
# import cv2  # Install opencv-python
import numpy as np
# from picamera2 import Picamera2
import time
import board
import neopixel_spi
from plant_monitor import PlantMonitor
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

print("1")

cred = credentials.Certificate('plantmonitor-19a40-firebase-adminsdk-8b656-f5000f8953.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://plantmonitor-19a40-default-rtdb.firebaseio.com'})
# firebase_admin.initialize_app(cred)
ref = db.reference("/")

print("2")

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
# model = load_model("keras_model.h5", compile=False)

# Load the labels
# class_names = open("labels.txt", "r").readlines()

# print("Initializing Monitor")
pm = PlantMonitor()
# print ("Monitor Initialized")

# CAMERA can be 0 or 1 based on default camera of your computer
# camera = cv2.VideoCapture(0)
# pi_camera = Picamera2()
# config = pi_camera.create_preview_configuration(main={"format": "RGB888"})
# pi_camera.configure(config)
# pi_camera.start()
time.sleep(1)

pixels = neopixel_spi.NeoPixel_SPI(board.SPI(), 50)

monitorValues = [0, 0, 0]

print("3")

def update_readings(): # update fields with new temp and eCO2 readings
    while True:
        monitorValues[0] = pm.get_wetness()
        monitorValues[1] = pm.get_temp()
        monitorValues[2] = pm.get_humidity()

while True:
    # Grab the webcamera's image.
    # ret, image = camera.read()
    # image = pi_camera.capture_array()
    # print(image)

    # Resize the raw image into (224-height,224-width) pixels
    # image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    # cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    # image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    # image = (image / 127.5) - 1

    # Predicts the model
    # prediction = model.predict(image)
    # index = np.argmax(prediction)
    # class_name = class_names[index]
    # confidence_score = prediction[0][index]

    # Gets Monitor readings
    # print("reading monitor")
    # monitorValues[0] = pm.get_wetness()
    # print(str(monitorValues[0]) + "% Moisture")
    print("4")
    update_readings()
    print(monitorValues)

    # Lights LEDs
    if monitorValues[0] < 15:
        pixels.fill(0x500000)
    elif monitorValues[0] < 30:
        pixels.fill(0x005000)
    else:
        pixels.fill(0x000050)

    dictionary = {
        'Plant1': {'humidity': monitorValues[2], 'temperature': monitorValues[1], 'moisture': monitorValues[0]}
    }  

    with open("test.json", "w") as outfile:
        json.dump(dictionary, outfile)

    with open("test.json", "r") as f:
	    file_contents = json.load(f)
    ref.set(file_contents)
    # Print prediction and confidence score
    # print("Class:", class_name[2:], end="")
    # print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
    # print(class_name[2:] + " (" + str(np.round(confidence_score * 100))[:-2] + "%)")

    # Listen to the keyboard for presses.
    # keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    # if keyboard_input == 27:
        # break
    
    # time.sleep(5)

# camera.release()
# cv2.destroyAllWindows()
