// filepath: /c:/Users/arman/Documents/GitHub/AdaptAI/src/frontend/app.js
async function generateResponse() {
    const prompt = document.getElementById('prompt').value;
    const chatBox = document.getElementById('chat-box');
    const loading = document.getElementById('loading');

    if (!prompt.trim()) return;

    // Create user message element
    const userMessageElement = document.createElement('div');
    userMessageElement.classList.add('message', 'user');
    userMessageElement.innerHTML = `<p><strong>You:</strong> ${prompt}</p>`;

    // Append user message to the chat box
    chatBox.appendChild(userMessageElement);

    // Clear the input
    document.getElementById('prompt').value = '';

    // Create typing indicator
    const typingIndicator = document.createElement('div');
    typingIndicator.classList.add('typing-indicator');
    typingIndicator.innerHTML = `
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
    `;

    // Append typing indicator to the chat box
    chatBox.appendChild(typingIndicator);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;

    // Simulate an AI response
    setTimeout(() => {
        // Remove typing indicator
        chatBox.removeChild(typingIndicator);

        const response = `AI Response to: "${prompt}"`;

        // Create AI message element
        const aiMessageElement = document.createElement('div');
        aiMessageElement.classList.add('message', 'ai');
        aiMessageElement.innerHTML = `<p><strong>AI:</strong> ${response}</p>`;

        // Append AI message to the chat box
        chatBox.appendChild(aiMessageElement);

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 1000); // Simulate a delay for AI response
}

function clearChat() {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML = '';
}