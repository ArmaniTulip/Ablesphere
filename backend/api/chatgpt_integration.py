import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Load OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')

# Example function to call OpenAI API
def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    user_input = input("Enter your question: ")
    response = get_openai_response(user_input)
    print("Response:", response)

