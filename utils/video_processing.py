import os
import requests
from gtts import gTTS
from mutagen.mp3 import MP3
from utils.pexels_api import get_videos
from moviepy import VideoFileClip, concatenate_videoclips, AudioFileClip
#from moviepy.audio.AudioClip import CompositeAudioClip

VIDEO_DIR = 'static/videos'
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

def process_segment(segment):
    # audio_path = f"static/{segment['segment_number']}.mp3"
    audio_path = os.path.join(VIDEO_DIR,f"{segment['segment_number']}.mp3")
    tts = gTTS(text=segment['text'])
    tts.save(audio_path)
    
    audio = MP3(audio_path)
    audio_length = round(audio.info.length)

    video_dist = get_videos(segment['prompt'], limit=audio_length)

    videos = []
    for i, video in enumerate(video_dist):
        # video_path = f"static/_{i+1}.mp4"
        video_path = os.path.join(VIDEO_DIR,f"_{i+1}.mp4")
        download_video(video['link'], video_path)
        
        video_clip = VideoFileClip(video_path)
        video_clip_trimmed = video_clip.subclipped(video['start'], video['end'])
        
        # Match resolution and FPS to the first video (reference)
        # if videos:
        #     ref_clip = videos[0]
        #     video_clip = video_clip.resized(ref_clip.size)  # Match resolution
        #     video_clip = video_clip.with_fps(ref_clip.fps)  # Match FPS
        video_clip_trimmed = video_clip_trimmed.resized((640,360))
        
        # trimmed_path = f"static/_t{i+1}.mp4"
        trimmed_path = os.path.join(VIDEO_DIR,f"_t{i+1}.mp4")
        video_clip_trimmed.write_videofile(trimmed_path)
        video_clip.close()
        video_clip_trimmed.close()
        videos.append(VideoFileClip(trimmed_path))

    final_video = concatenate_videoclips(videos)
    # segment_video_path = f"static/{segment['segment_number']}.mp4"
    segment_video_path = os.path.join(VIDEO_DIR,f"{segment['segment_number']}.mp4")
    final_video.write_videofile(segment_video_path)

    audio_clip = AudioFileClip(audio_path)
    if audio_clip.duration < final_video.duration:
        final_video = final_video.subclipped(0, audio_clip.duration)
    else:
        audio_clip = audio_clip.subclipped(0, final_video.duration)


    final_video = final_video.with_audio(audio_clip)
    # output_path = f"static/a{segment['segment_number']}.mp4"
    output_path = os.path.join(VIDEO_DIR,f"a{segment['segment_number']}.mp4")
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close all loaded clips to free memory
    for clip in videos + [final_video, audio_clip]:
        clip.close()

    return output_path

def make_video(json_obj:dict):

    videos = []
    for segment in json_obj['segments']:
        videos.append(VideoFileClip(process_segment(segment)))

    final_video = concatenate_videoclips(videos)
    final_video_path = os.path.join(VIDEO_DIR,"final.mp4")
    final_video.write_videofile(final_video_path, codec="libx264", audio_codec="aac")

    # Close final merged clips
    for video in videos:
        video.close()

    for file in os.listdir(VIDEO_DIR):
        if file != 'final.mp4':
            os.remove(os.path.join(VIDEO_DIR,file))

    return final_video_path