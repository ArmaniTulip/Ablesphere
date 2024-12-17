# server.py
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import openai
from api_routes import setup_routes

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

app = Flask(__name__)
setup_routes(app)

@app.route('/api/task_prompt', methods=['POST'])
def task_prompt():
    data = request.json
    user_input = data.get('task', '')
    response = get_openai_response(user_input)
    return jsonify({"response": response})

@app.route('/api/frustration', methods=['POST'])
def frustration():
    data = request.json
    frustration_level = data.get('frustration_level', 0)

    if frustration_level > 5:
        return jsonify({"intervention": "Take a deep breath and count to 10. You can do it!"})
    else:
        return jsonify({"intervention": "You're doing great! Keep it up."})

user_data = {}

@app.route('/api/adaptive', methods=['POST'])
def adaptive():
    user = request.json.get('user', 'default')
    if user not in user_data:
        user_data[user] = {"tasks_completed": 0}

    user_data[user]["tasks_completed"] += 1

    if user_data[user]["tasks_completed"] > 3:
        message = "You're on fire! Keep up the great work!"
    else:
        message = "Keep going! You're making progress."

    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)
