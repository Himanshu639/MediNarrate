import requests as req
import json
import os
from dotenv import load_dotenv
load_dotenv()

class mistral_ai:
    # - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - Variables - - - - - - - - -
    key = os.getenv('MISTRAL_API')
    url = 'https://api.mistral.ai'
    models = {
        1: 'ministral-8b-2410',
        2: 'ministral-8b-latest',
        3: 'mistral-tiny' 
    }
    # - - - - - - - - - - - - - - - - - - - - - - -
    # - - - - - - - - - Functions - - - - - - - - -
    def call_mistral_ai(self, end_point, method, payload=None):
        headers={"Authorization" : 'Bearer '+ self.key, "Content-Type" : "application/json"}
        if method=='get':
            res = req.get(f'{self.url}/{end_point}',headers=headers,json=payload).content
        elif method=='post':
            res = req.post(f'{self.url}/{end_point}',headers=headers,json=payload).content

        return json.loads(res)

    def get_models(self):
        res = self.call_mistral_ai('v1/models','get')
        model_list = [model['id'] for model in res['data']]
        return json.dumps(model_list,indent=4)

    def chat_completion(self,msg,model_id):
        payload = {
            "model": self.models[model_id],  
            "messages": [
                {
                    "role": "user",
                    "content": msg
                }
            ]
        }
        res = self.call_mistral_ai('v1/chat/completions','post',payload=payload)
        return res['choices'][0]['message']['content']

    def retrive_model_info(self,model_id):
        res = self.call_mistral_ai(f'v1/models/{self.models[model_id]}','get')
        return json.dumps(res,indent=4)


if __name__ == '__main__':
    gpt = mistral_ai()
    prompt = 'Start writing dictionary of english words with their meaning in short sentence until your token limit is reached, which means you have to try to output as many words as you can'
    response = gpt.chat_completion(prompt,2)
    print(response)
