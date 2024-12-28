from utils.mistral_ai import mistral_ai
from utils.pexels_api import get_videos
from gtts import gTTS
from mutagen.mp3 import MP3
from moviepy import VideoFileClip, concatenate_videoclips, AudioFileClip
#from moviepy.audio.AudioClip import CompositeAudioClip
import requests
import json

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

gpt = mistral_ai()
with open('utils/template.txt', 'r') as file:
    template = file.read()

with open('utils/text.txt','r') as file:
    text = file.read()

prompt = template + text
response = gpt.chat_completion(prompt,1)

json_obj = json.loads(response[7:-3])

print(json.dumps(json_obj,indent=4))

def process_segment(segment):
    # Save TTS audio
    audio_path = f"static/{segment['segment_number']}.mp3"
    tts = gTTS(text=segment['text'])
    tts.save(audio_path)
    
    # Load audio and get its length
    audio = MP3(audio_path)
    audio_length = round(audio.info.length)

    # Get relevant videos for the prompt
    video_dist = get_videos(segment['prompt'], limit=audio_length)

    # Download and process videos
    videos = []
    for i, video in enumerate(video_dist):
        video_path = f"static/_{i+1}.mp4"
        download_video(video['link'], video_path)
        
        # Load video and ensure proper properties
        video_clip = VideoFileClip(video_path)
        video_clip = video_clip.subclipped(video['start'], video['end'])
        
        # Match resolution and FPS to the first video (reference)
        # if videos:
        #     ref_clip = videos[0]
        #     video_clip = video_clip.resized(ref_clip.size)  # Match resolution
        #     video_clip = video_clip.with_fps(ref_clip.fps)  # Match FPS
        video_clip = video_clip.resized((640,360))
        
        # Save the trimmed video
        trimmed_path = f"static/_t{i+1}.mp4"
        video_clip.write_videofile(trimmed_path)
        videos.append(VideoFileClip(trimmed_path))

    # Concatenate videos
    final_video = concatenate_videoclips(videos)
    segment_video_path = f"static/{segment['segment_number']}.mp4"
    final_video.write_videofile(segment_video_path)

    # Adjust audio and video durations
    audio_clip = AudioFileClip(audio_path)
    if audio_clip.duration < final_video.duration:
        final_video = final_video.subclipped(0, audio_clip.duration)
    else:
        audio_clip = audio_clip.subclipped(0, final_video.duration)

    # Add audio to video
    final_video = final_video.with_audio(audio_clip)
    output_path = f"static/a{segment['segment_number']}.mp4"
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close all loaded clips to free memory
    for clip in videos + [final_video, audio_clip]:
        clip.close()

    return output_path


# Process all segments
videos = []
for segment in json_obj['segments']:
    videos.append(VideoFileClip(process_segment(segment)))

# Merge final video
final_video = concatenate_videoclips(videos)
final_video.write_videofile("static/final.mp4", codec="libx264", audio_codec="aac")

# Close final merged clips
for video in videos:
    video.close()



    