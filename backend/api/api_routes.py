from flask import Blueprint, request, jsonify
from .chatgpt_integration import get_chatgpt_response

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/api/chat', methods=['POST'])

def chat():
    try:
        data = request.get_json()
        message = data.get('message')
        if not message:
            return jsonify({'error': 'No message provided'}), 400

        response = get_chatgpt_response(message)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500