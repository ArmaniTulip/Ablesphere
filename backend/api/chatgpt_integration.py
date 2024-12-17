import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Your OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')

# Example function to call OpenAI API
def get_openai_response(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
