# MN-1st-build

This build is essential part of MediNarriate project, this build accomplishes the gathering of videos and also combining in the end.
This part of project goes through following process.



## Working
### 1) Splitting the text into segments(chunks)
- The text is getting splitted into number of segments based on theme of story(text). Essentially it uses [Mistral AI GPT](https://docs.mistral.ai/api/) model to split into the segments and it also gives keywords to describe the scenario in the text(story).
- The GPT model has given this [prompt](utils/template.txt) to make segments and also well describing each text segment.
- The response from GPT model is prompted to be in JSON format like this
```json
{  
  "segments": [  
    {  
      "segment_number": 1,  
      "prompt": "Generalized visual description with relevant keywords",  
      "text": "Enhanced narrative text for the segment."  
    },  
    {  
      "segment_number": 2,  
      "prompt": "Next generalized visual description",  
      "text": "Next enhanced narrative text."  
    }  
  ]  
}
```
- Here, the `prompt` actually contains the relevant keywords for each segment and `text` contains narrative description for each segment.

### 2) Generating audio file for each segment
- Generation of audio is getting carried out by [gTTS](https://pypi.org/project/gTTS/) (Google Text-to-Speech).
- The program simply converts `text` of each segment into corresponding audio.

### 3) Fetching videos
- [Pexels](https://www.pexels.com/api/) is a popular website offering a vast library of high-quality, royalty-free stock photos and videos.
- So, fetching relevant videos for each segment is done by [Pexels](https://www.pexels.com/api/) API.
- Here, in the program, not only fetching is done but also calculating how much video to trim and how much to keep to match audio length for each segment.

### 4) Combining video with audio
- Now, we have audio and video for each segment, so in this step, combining them to together using [moviepy](https://pypi.org/project/moviepy/).

### 5) Combining videos from each segment into one video
- Lastly, we have videos from each segment, again using [moviepy](https://pypi.org/project/moviepy/) to combine them into one.

## Installation and setup

### Step 1:
- To download this repository, use following command:
```bash
git clone https://github.com/Himanshu639/MN-1st-build.git
```

### Step 2: 
- Make sure you have python installed (>=3.11).
- You can check your Python version by running following command:
  `python --version`
- Or if you use Python3 explicitly, then following command will show the version `python3 --version`

### Step 3(Optionally): 
- Create a virtual environment for this project using this command `python -m venv <virtual_env_name>`.
- To activate the virtual environment
  - On windows
    ```powershell
    .\<virtual_env_name>\Scripts\activate
    ```
  - On linux
    ```bash
    source <virtual_env_name>/bin/activate

### Step 4:
- Install the requirements for this project to run by running following command:
  ```bash
  pip install -r requirements.txt
  ```

### Step 5:
- Generate API Keys for [Pexels Video API](https://www.pexels.com/api/) and [Mistral AI GPT](https://docs.mistral.ai/api/).
- Make .env file and add following lines
```
MISTRAL_API=<YOUR_MISTRAL_AI_API_KEY>
PEXELS_API=<YOUR_PEXELS_API_KEY>
```

### Step 6:
- Run the main.py by following command: `python main.py`.
- Output will be in static folder named as `final.mp4`
