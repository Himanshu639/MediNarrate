from utils.pexels_api import get_videos
import json
import requests
from moviepy import VideoFileClip, concatenate_videoclips

def download_video(video_url, file_name):
    response = requests.get(video_url, stream=True)

    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            # Download the video in chunks to avoid memory overload
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")

video_dist = get_videos('a man working on computer',22)
print(json.dumps(video_dist,indent=4))

# print(type(video_dist[1]['start']))


for i,video in enumerate(video_dist):
    path = f'static/{i}.mp4'
    download_video(video['link'],path)
    video_clip = VideoFileClip(path)

    start = video['start']
    end = video['end']
    trimmed_video = video_clip.subclipped(start,end)
    trimmed_video.write_videofile(f'static/trimmed{i}.mp4')


videos = [VideoFileClip(f'static/trimmed{i}.mp4') for i in range(len(video_dist))]

final_video = concatenate_videoclips(videos)
final_video.write_videofile(f'static/final.mp4')
