from flask import Flask, request, jsonify
from chatgpt_integration import get_openai_response

def setup_routes(app):
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

    @app.route('/api/chat', methods=['POST'])
    def chat():
        data = request.json
        prompt = data.get('prompt', '')
        print(f"Received prompt: {prompt}")  # Log the received prompt
        try:
            response = get_openai_response(prompt)
            print(f"OpenAI response: {response}")  # Log the OpenAI response
            return jsonify({"response": response})
        except Exception as e:
            print(f"Error: {e}")  # Log any errors
            return jsonify({"error": str(e)}), 500
