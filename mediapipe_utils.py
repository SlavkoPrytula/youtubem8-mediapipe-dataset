import os
import sys
import json
import glob
import random
import collections
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mediapipe as mp
import cv2
import time

plt.style.use("dark_background")

DIRECTORY = "output_files"


def create_video(url: str, early_stopping=None):
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic

    # Error might be here
    cap = cv2.VideoCapture(url)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    dimensions = (int(cap.get(3)), int(cap.get(4)))
    fps = cap.get(cv2.CAP_PROP_FPS)
    video = cv2.VideoWriter(f"{DIRECTORY}/output_video.mp4", fourcc, fps, dimensions)

    print("Creating video...")
    start_time = time.time()

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            try:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                results = holistic.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(235, 149, 52), thickness=1, circle_radius=1),
                                          mp_drawing.DrawingSpec(color=(86, 52, 235), thickness=1, circle_radius=1),
                                          )
            except cv2.error:
                break

            video.write(image)

            if early_stopping:
                if (time.time() - start_time - 8) >= early_stopping:
                    print("Early ending")
                    break

    cap.release()
    video.release()
    print("Done!")

    # @staticmethod
    # def info_message(message, *args, end="\n"):
    #     print(message.format(*args), end=end)
