# youtubem8-mediapipe-dataset
70k video ids dataset for face tracking

# Idea

The project contains .txt in ```data_files/ids.txt``` file (the main file with video ids). You may add yout own by creating new rows in the file.

As for now the dataset contatins only videos of beauty salons topic

---
# Usage

The ```main.py``` program contains blocks of code you want to use.

```python
# face and beauty salon datasets
with open("data_files/ids.txt") as f:
    video_ids = [line for line in f]
    video_ids = sum([video_ids[i].split("[")[1].split("]")[0].replace('"', "").split(",")
                     for i in range(len(video_ids))], [])

```

This loads all the ids for later use.

---
# Results

```python
video_url = get_video_url(video_id=video_ids[100])
input_url = get_input_url(video_url)
create_video(input_url, early_stopping=40)
```

These three functions load the video from youtube by its unique id you specify yourself (ex. ```get_video_url(video_id=video_ids[100])```)

As the output you get the processed video by mediapipe baseline code. The code itself executes the face tracking and allows to save the processed file localy on yout device. 

```create_video(input_url, early_stopping=40)``` creates a video of face tracking by applying the landmarks on the face in the video. Then saves it. ``` early_stopping=40``` specifies how long (in seconds) you want to parse the video.

--- 
# Mediapipe

For your own use refer to the [mediapipe documentation](https://google.github.io/mediapipe/getting_started/python). Feel free to change the code under your needs.
