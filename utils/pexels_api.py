import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


key = os.getenv('PEXELS_API')

def get_videos(query:str, limit:int) -> list[dict[str:str, int]]:

    if limit < 4:
        raise ValueError("Parameter `limit` should be greater than or equal to 4")

    response = requests.get(url=f'https://api.pexels.com/videos/search?query={query}&orientation=landscape',
                            headers={"Authorization":key})

    json_res = json.loads(response.content)

    video_distribution = []
    duration = 0
    i = 0
    while duration<limit:
        current_duration = json_res['videos'][i]['duration']

        # Ensuring the video atleast of 8 seconds
        if current_duration >= 8:
            for file in json_res['videos'][i]['video_files']:
                if file['width'] == 640:
                    video_distribution.append({ "duration":current_duration,
                                                "link":file['link'],
                                                "start":0,
                                                "end":current_duration })
                    break
            duration+= current_duration

        i+=1

    # The last video will definetly be longer than we want or same as we want.
    # suppose we want to make 24 seconds video, and we have got videos of length [16,6,15].
    # Till second video, the combined video will be of 22 seconds, now we just want 2 seconds of additional video from 3rd video, but here is catch, if we just take a part of 2 seconds of 3rd video, it won't be that meaningful.
    # For that thing, I am going to implement a logic(code) that will trim the longest video(starting and ending [assuming starting and ending isn't important]) in the list of videos to fit the last video of 6 seconds.

    # Here, a new question arises, what part of 6 seconds should we take from the last video?
    # -> According to me, if we take 6 seconds from exactly in the middle ([mid-3.....mid.....mid+3] => makes 6 seconds) that would be a great choice because it will the most valueable content (again, assuming starting and ending isn't important)

    # Also, one more question, what part of longest video should we trim?
    # -> The assumption would be same (starting and ending doesn't hold that much value as of middle part), so triming from starting and ending would make sense

    

    
    required = limit - duration + current_duration 
    if required < 4:
        # Case 1: the video will be longer than we want and required time is less than 4 seconds
        # -> so, we will get the last video of 4 seconds from the center and trim the longest video from starting and ending ((whatever required/2) from both ends) from the list of videos 
        mid = current_duration/2
        video_distribution[-1]['start'] = mid - 2
        video_distribution[-1]['end'] = mid + 2

        max_len_video:dict = {'duration':-1}
        for video in video_distribution[:-1]:
            if max_len_video['duration'] < video['duration']:
                max_len_video = video
        
        max_len_video['start'] += (4 - required)/2
        max_len_video['end'] -= (4 - required)/2

    else:

        # Case 2: the video will be longer than we want and required time is more than 4 seconds
        # -> we will get the last video of whatever required from center of video.
        mid = current_duration/2
        video_distribution[-1]['start'] = mid - (required/2)
        video_distribution[-1]['end'] = mid + (required/2)
        # eg. 6 seconds -> 2 seconds trim from middle
        # 0 1 (2 3 4) 5 6 -> 2 to 4 -> mid = length/2 -> mid-(req/2) to mid+(req/2)
        # eg. 7 seconds -> 2 seconds trim from middle
        # 0 1 2 (2.5 3 4 4.5) 5 6 7 -> 2.5 to 4.5 -> mid = length/2 -> mid-(req/2) to mid+(req/2)
    
    return video_distribution

if __name__=='__main__':
    video_dist = get_videos('communication',22)
    print(json.dumps(video_dist,indent=4))

# ->>  <=>  
