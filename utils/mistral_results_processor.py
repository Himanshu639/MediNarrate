from utils.mistral_ai import mistral_ai
import json

def generate_and_preprocess(text:str) -> dict:
    
    with open('utils/prompt.txt', 'r') as file:
        prompt = file.read()

    full_prompt = prompt + text

    gpt = mistral_ai()
    response = gpt.chat_completion(full_prompt,1)
    print(response)

    json_obj = json.loads(response[7:-3])

    return json_obj