import openai
import os

openai.api_key = str(os.environ.get('OPENAI_API_KEY'))

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

### OPEN AI CONFIGURATION ###
MODEL_NAME = "text-davinci-003"
MODEL_TEMPERATURE = 0
MODEL_MAX_TOKENS = 500

def model_output(prompt, model=MODEL_NAME, temperature=MODEL_TEMPERATURE, max_tokens=MODEL_MAX_TOKENS):
    response = openai.Completion.create(model=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens)
    return response.choices[0]['text']