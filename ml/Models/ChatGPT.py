#Create Flask Backend create (server.py) file
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/task_prompt', methods=['POST'])
def task_prompt():
    data = request.json
    user_input = data.get('task', '')
    response = f"Let's get started on: {user_input}! Here's a tip to help you: Start with an outline."
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
#Frontend HTML/JavaScript:Create (index.html):
<input type="text" id="taskInput" placeholder="Enter your task">
<button id="sendTask">Send Task</button>
<div id="response"></div>

<script>
  document.getElementById('sendTask').addEventListener('click', async () => {
    const task = document.getElementById('taskInput').value;
    const response = await fetch('http://127.0.0.1:5000/api/task_prompt', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ task })
    });
    const data = await response.json();
    document.getElementById('response').innerText = data.response;
  });
</script>
#Run Your Server
#Start the Flask server:
python server.py
#Open the index.html file in a browser. Test the input by typing a task and pressing the button.   
#Task 2: Integrating the ChatGPT API
#Install the OpenAI Python Library:
pip install openai
#Set Up API Key:
#Get an API key from OpenAI.
#Store it in a .env file for security:
OPENAI_API_KEY=your_api_key_here
#Install python-dotenv:
pip install python-dotenv
#Load the key in your backend:
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
#Update Flask Endpoint:
@app.route('/api/task_prompt', methods=['POST'])
def task_prompt():
    data = request.json
    user_input = data.get('task', '')

    # Call ChatGPT API
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=f"Motivate a student to complete this task: {user_input}",
        max_tokens=50
    )

    return jsonify({"response": response.choices[0].text.strip()})
#Test Integration:
#Restart your server.
#Use the same frontend setup as Task 1. Test if the responses come from ChatGPT.
#Task 3: Distraction Detection and Blocking
#Objective: Detect web usage and redirect focus to coursework.
#steps
#1.Frontend Check
#Simulate distraction detection with JavaScript
<button id="startWork">Start Work</button>
<div id="focusAlert"></div>

<script>
  let distractionCount = 0;

  function detectDistraction() {
    distractionCount++;
    if (distractionCount > 2) {
      document.getElementById('focusAlert').innerText = "Focus on your work!";
    }
  }

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      detectDistraction();
    }
  });

  document.getElementById('startWork').addEventListener('click', () => {
    distractionCount = 0;
    document.getElementById('focusAlert').innerText = "Good job! You're on track.";
  });
</script>
#Task 4: Frustration Detection
#Objective: Use simulated behavior to detect frustration and provide interventions.
#steps
#1.Backend Logic:
@app.route('/api/frustration', methods=['POST'])
def frustration():
    data = request.json
    frustration_level = data.get('frustration_level', 0)

    if frustration_level > 5:
        return jsonify({"intervention": "Take a deep breath and count to 10. You can do it!"})
    else:
        return jsonify({"intervention": "You're doing great! Keep it up."})
#2.Frontend Simulation
  <button id="simulateFrustration">Simulate Frustration</button>
<div id="intervention"></div>

<script>
  let frustrationLevel = 0;

  document.getElementById('simulateFrustration').addEventListener('click', async () => {
    frustrationLevel += 1;

    const response = await fetch('http://127.0.0.1:5000/api/frustration', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ frustration_level: frustrationLevel })
    });

    const data = await response.json();
    document.getElementById('intervention').innerText = data.intervention;
  });
</script>
  #Task 5: Adaptive Behavior
#Objective: Store patterns and adjust suggestions dynamically.
#Steps
#1.Backend Updates
#Add a dictionay to track completion:
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

    
