from utils.mistral_ai import mistral_ai
from utils.ocr import get_text
from utils.video_processing import make_video
import json
import os

if 'static' not in os.listdir():
    os.makedirs('static')


gpt = mistral_ai()
with open('utils/template.txt', 'r') as file:
    template = file.read()

# with open('utils/text.txt','r') as file:
#     text = file.read()
text = get_text('utils/text.jpg')

prompt = template + text
response = gpt.chat_completion(prompt,1)
print(response)

json_obj = json.loads(response[7:-3])


make_video(json_obj=json_obj)