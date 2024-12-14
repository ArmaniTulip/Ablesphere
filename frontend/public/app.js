// filepath: /c:/Users/arman/Documents/GitHub/AdaptAI/src/frontend/app.js
async function generateResponse() {
    const prompt = document.getElementById('prompt').value;
    const chatBox = document.getElementById('chat-box');

    // Simulate an AI response for now
    const response = `AI Response to: "${prompt}"`;

    // Create a new message element
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.innerText = response;

    // Append the message to the chat box
    chatBox.appendChild(messageElement);

    // Clear the input
    document.getElementById('prompt').value = '';

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}