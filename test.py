import os
import requests
from dotenv import load_dotenv
from openai import OpenAI



system_prompt = "You are an assistant that analyzes the question given and respond in a shor answer. \
Respond in markdown."


# Open and configure OpenAI client
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
else:
    print("API key found and looks good so far!")

openai = OpenAI()
texto_usuario='What is the capital of France?'
# set the system prompt
messages = [
{"role": "system", "content": system_prompt},
{"role": "user", "content": texto_usuario}
]

# Call the OpenAI API
response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
response_text = response.choices[0].message.content

print(response_text)
