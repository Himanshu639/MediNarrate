from langchain_groq import ChatGroq
import json
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    temperature = 0,
    groq_api_key = os.getenv('GROQ_API'),
    model_name = "llama-3.3-70b-versatile"
)

def generate_and_preprocess(text:str) -> dict:
    with open('utils/prompt.txt', 'r') as file:
        prompt = file.read()

    full_prompt = prompt + text
    response = llm.invoke(full_prompt).content
    print(response)

    json_obj = json.loads(response[7:-3])

    return json_obj

if __name__ == "__main__":
    print(llm.invoke("Hello World!").content)