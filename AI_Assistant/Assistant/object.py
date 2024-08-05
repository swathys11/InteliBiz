# from django.conf import settings
# from django.shortcuts import render
# from django.http import JsonResponse
# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia
# import pyjokes
# import requests
# from gtts import gTTS
# from playsound import playsound
# import os
# import cv2
# import numpy as np

# def talk(text):
#     tts = gTTS(text=text, lang='en')
#     audio_file_path = os.path.join(settings.MEDIA_ROOT, 'speech.mp3')
#     tts.save(audio_file_path)
#     return settings.MEDIA_URL + 'speech.mp3'


# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# def start_object_detection():
#     # Update these paths to the actual locations of the files
#     model_prototxt = os.path.join(settings.BASE_DIR, 'C:\Users\swath\OneDrive\Desktop\Vission_speak\AI_Assistant\models/deploy.prototxt')
#     model_caffemodel = os.path.join(settings.BASE_DIR, 'C:\Users\swath\OneDrive\Desktop\Vission_speak\AI_Assistant\models/mobilenet_iter_73000.caffemodel')

#     # Check if the files exist
#     if not os.path.isfile(model_prototxt):
#         raise FileNotFoundError(f"Prototxt file not found at path: {model_prototxt}")
#     if not os.path.isfile(model_caffemodel):
#         raise FileNotFoundError(f"Caffemodel file not found at path: {model_caffemodel}")

#     # Load the MobileNetSSD model
#     net = cv2.dnn.readNetFromCaffe(model_prototxt, model_caffemodel)
#     cap = cv2.VideoCapture(0)  # Open the webcam

#     CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", 
#                "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
#                "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
#                "sofa", "train", "tvmonitor"]

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         (h, w) = frame.shape[:2]
#         blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
#         net.setInput(blob)
#         detections = net.forward()

#         for i in range(detections.shape[2]):
#             confidence = detections[0, 0, i, 2]
#             if confidence > 0.2:
#                 idx = int(detections[0, 0, i, 1])
#                 box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
#                 (startX, startY, endX, endY) = box.astype("int")
#                 label = f"{CLASSES[idx]}: {confidence * 100:.2f}%"
#                 cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
#                 y = startY - 15 if startY - 15 > 15 else startY + 15
#                 cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#         cv2.imshow('Object Detection', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
    
# def handle_command(command):
    
    
#     if 'open camera' in command:
#         start_object_detection()
#         return talk('Opening camera for object detection.')

#     else:
#         return talk('Please say that command again.')





import cv2
import numpy as np


# Update with the absolute paths to your files
deploy_prototxt_path = r'C:\Users\swath\OneDrive\Desktop\Vission_speak\AI_Assistant\models\deploy.prototxt'
mobilenet_model_path = r'C:\Users\swath\OneDrive\Desktop\Vission_speak\AI_Assistant\models\mobilenet_iter_73000.caffemodel'

try:
    with open(deploy_prototxt_path, 'r') as file:
        print("deploy.prototxt is accessible")
    with open(mobilenet_model_path, 'rb') as file:
        print("mobilenet_iter_73000.caffemodel is accessible")
except Exception as e:
    print(f"File access error: {e}")

# Load the class labels
class_labels = [
    'background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 
    'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 
    'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
]

# Initialize video capture (0 for webcam or replace with video file path)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (127.5, 127.5, 127.5))
    ret.setInput(blob)
    detections = ret.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.2:  # Adjust confidence threshold as needed
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            label = class_labels[int(detections[0, 0, i, 1])]
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}: {confidence:.2f}", (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Object Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
