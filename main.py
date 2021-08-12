from tfrecords_utils import get_video_url
from youtube_utils import get_input_url
from mediapipe_utils import create_video
from functools import reduce


# video_url = 'https://www.youtube.com/watch?v=RvO7SqcVJtw'
# video_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"

# face and beauty salon datasets
with open("data_files/ids.txt") as f:
    video_ids = [line for line in f]
    video_ids = sum([video_ids[i].split("[")[1].split("]")[0].replace('"', "").split(",")
                     for i in range(len(video_ids))], [])

# video_url = get_video_url(video_id=video_ids[100])
# input_url = get_input_url(video_url)
# create_video(input_url, early_stopping=40)
