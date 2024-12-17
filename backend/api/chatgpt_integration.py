import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

