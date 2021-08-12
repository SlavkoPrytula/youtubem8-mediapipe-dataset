import tensorflow as tf
from IPython.display import YouTubeVideo

import os
import cv2
import mediapipe as mp
import youtube_dl
import keyboard

from bs4 import BeautifulSoup as beautiful_soup
import requests

import matplotlib.pyplot as plt
plt.style.use("dark_background")

DIRECTORY = "/home/slavko/data/yt8m/video/"


def get_video_url(file_index=None, video_id=None) -> str:
    # check if video is good
    if not video_id:
        video_id = get_video_id(file_index)
    url_id = extract_url(video_id)
    video_url = f"https://www.youtube.com/watch?v={url_id}"

    return video_url


def get_video_id(file_index):
    directories = os.listdir(DIRECTORY)[1:]
    record = directories[file_index]
    video_lvl_record = DIRECTORY + record

    vid_ids = []
    labels = []
    mean_rgb = []
    mean_audio = []

    for example in tf.compat.v1.io.tf_record_iterator(video_lvl_record):
        tf_example = tf.train.Example.FromString(example)

        vid_ids.append(tf_example.features.feature['id'].bytes_list.value[0].decode(encoding='UTF-8'))
        labels.append(tf_example.features.feature['labels'].int64_list.value)
        mean_rgb.append(tf_example.features.feature['mean_rgb'].float_list.value)
        mean_audio.append(tf_example.features.feature['mean_audio'].float_list.value)

    print('Number of videos in this tfrecord: ', len(mean_rgb))
    print('Picking a youtube video id:', vid_ids[0])
    print('First 20 features of a youtube video (', vid_ids[0], '):')
    print(mean_rgb[0][:20])

    video_id = vid_ids[0]
    return video_id


def extract_url(video_id):
    db_url = f"https://storage.googleapis.com/data.yt8m.org/2/j/i/{video_id[0:2]}/{video_id}.js"
    res = requests.get(db_url)
    html_page = res.content
    soup = beautiful_soup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    try:
        url = text[0].split('"')[-2]
    except IndexError as e:
        raise Exception(f"Couldn't find video")

    return url
