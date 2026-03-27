from flask import Flask, request, jsonify, Blueprint
from chatgpt_integration import get_openai_response

api_bp = Blueprint('api', __name__)

def setup_routes(app):
    app.register_blueprint(api_bp)

    @api_bp.route('/task_prompt', methods=['POST'])
    def task_prompt():
        data = request.json
        user_input = data.get('task', '')
        response = get_openai_response(user_input)
        return jsonify({"response": response})

    @api_bp.route('/frustration', methods=['POST'])
    def frustration():
        data = request.json
        frustration_level = data.get('frustration_level', 0)

        if frustration_level > 5:
            return jsonify({"intervention": "Take a deep breath and count to 10. You can do it!"})
        else:
            return jsonify({"intervention": "You're doing great! Keep it up."})

    user_data = {}

    @api_bp.route('/adaptive', methods=['POST'])
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

    @api_bp.route('/chat', methods=['POST'])
    def chat():
        data = request.json
        prompt = data.get('prompt', '')
        log_received_prompt(prompt)
        try:
            response = get_chatgpt_response(prompt)
            log_openai_response(response)
            return jsonify({"response": response})
        except Exception as e:
            log_error(e)
            return jsonify({"error": str(e)}), 500

    def log_received_prompt(prompt):
        print(f"Received prompt: {prompt}")  # Log the received prompt

    def log_openai_response(response):
        print(f"OpenAI response: {response}")  # Log the OpenAI response

    def log_error(error):
        print(f"Error: {error}")  # Log any errors

    def get_chatgpt_response(prompt):
        return get_openai_response(prompt)

    @api_bp.route('/upload_iep', methods=['POST'])
    def upload_iep():
        if 'iep' not in request.files:
            return jsonify({"message": "No file part"}), 400

        file = request.files['iep']

        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400

        # if file:
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join('uploads', filename))
        #     return jsonify({"message": "IEP uploaded successfully"}), 200
