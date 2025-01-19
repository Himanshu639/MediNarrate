from utils.mistral_ai import mistral_ai
import json

def generate_and_preprocess(text:str) -> dict:
    
    with open('utils/template.txt', 'r') as file:
        template = file.read()

    gpt = mistral_ai()
    prompt = template + text
    response = gpt.chat_completion(prompt,1)
    print(response)

    json_obj = json.loads(response[7:-3])

    return json_obj