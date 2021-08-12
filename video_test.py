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
import seaborn as sns

import torch
from torch import nn
from torch.utils import data as torch_data
from sklearn import model_selection as sk_model_selection
from torch.nn import functional as torch_functional
import torch.nn.functional as F
from torchvision import transforms, utils

from sklearn import model_selection
from sklearn import metrics
from skimage import exposure

from albumentations import Resize, Normalize, Compose
from albumentations.pytorch import ToTensorV2
import albumentations as album

import warnings

warnings.filterwarnings("ignore")
plt.style.use("dark_background")

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score

import mediapipe as mp
import cv2


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture("vid_01.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('output.avi', 0, 20.0, (320, 240))
# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
# video = cv2.VideoWriter('output.mp4', fourcc, 20.0, (320, 240))

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()
        try:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = holistic.process(image)
            print(results.face_landmarks)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(235, 149, 52), thickness=1, circle_radius=1),
                                      mp_drawing.DrawingSpec(color=(86, 52, 235), thickness=1, circle_radius=1),
                                      )
        except cv2.error:
            break

        video.write(image)

        # plt.imshow(image)
        # plt.show()
        # break

cap.release()
# cv2.destroyAllWindows()
print("Done!")




