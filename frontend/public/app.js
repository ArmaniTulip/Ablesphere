async function generateResponse() {
    const prompt = document.getElementById('prompt').value;
    const chatBox = document.getElementById('chat-box');

    if (!prompt.trim()) return;

    // Create user message element
    const userMessageElement = document.createElement('div');
    userMessageElement.classList.add('message', 'user');
    userMessageElement.innerHTML = `<p><strong>You:</strong> ${prompt}</p>`;

    // Apply current theme to the new message
    if (document.body.classList.contains('dark')) {
        userMessageElement.classList.add('dark');
    } else {
        userMessageElement.classList.add('light');
    }

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

    // Apply current theme to the typing indicator
    if (document.body.classList.contains('dark')) {
        typingIndicator.classList.add('dark');
    } else {
        typingIndicator.classList.add('light');
    }

    // Append typing indicator to the chat box
    chatBox.appendChild(typingIndicator);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        // Fetch AI response
        const response = await fetch('http://127.0.0.1:5000/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        // Remove typing indicator
        chatBox.removeChild(typingIndicator);

        // Create AI message element
        const aiMessageElement = document.createElement('div');
        aiMessageElement.classList.add('message', 'ai');
        aiMessageElement.innerHTML = `<p><strong>AI:</strong> ${data.response}</p>`;

        // Apply current theme to the new message
        if (document.body.classList.contains('dark')) {
            aiMessageElement.classList.add('dark');
        } else {
            aiMessageElement.classList.add('light');
        }

        // Append AI message to the chat box
        chatBox.appendChild(aiMessageElement);

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        console.error('Error fetching AI response:', error);

        // Remove typing indicator
        chatBox.removeChild(typingIndicator);

        // Show error message
        const errorMessageElement = document.createElement('div');
        errorMessageElement.classList.add('message', 'error');
        errorMessageElement.innerHTML = `<p><strong>Error:</strong> Failed to fetch AI response. Please try again later.</p>`;

        // Apply current theme to the error message
        if (document.body.classList.contains('dark')) {
            errorMessageElement.classList.add('dark');
        } else {
            errorMessageElement.classList.add('light');
        }

        // Append error message to the chat box
        chatBox.appendChild(errorMessageElement);

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

function clearChat() {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML = '';
}

function toggleTheme() {
    const body = document.body;
    const header = document.querySelector('header');
    const chatContainer = document.getElementById('chat-container');
    const chatBox = document.getElementById('chat-box');
    const textarea = document.querySelector('textarea');
    const buttons = document.querySelectorAll('button');
    const dots = document.querySelectorAll('.dot');
    const messages = document.querySelectorAll('.message');
    const themeLabel = document.getElementById('theme-label');
    const sections = document.querySelectorAll('section');

    body.classList.toggle('dark');
    body.classList.toggle('light');
    header.classList.toggle('dark');
    header.classList.toggle('light');
    chatContainer.classList.toggle('dark');
    chatContainer.classList.toggle('light');
    chatBox.classList.toggle('dark');
    chatBox.classList.toggle('light');
    textarea.classList.toggle('dark');
    textarea.classList.toggle('light');
    buttons.forEach(button => {
        button.classList.toggle('dark');
        button.classList.toggle('light');
    });
    dots.forEach(dot => {
        dot.classList.toggle('dark');
        dot.classList.toggle('light');
    });
    messages.forEach(message => {
        message.classList.toggle('dark');
        message.classList.toggle('light');
    });
    sections.forEach(section => {
        section.classList.toggle('dark');
        section.classList.toggle('light');
    });

    // Update theme label
    if (body.classList.contains('dark')) {
        themeLabel.textContent = 'Dark Mode';
    } else {
        themeLabel.textContent = 'Light Mode';
    }
}

// Task Prompt
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

// Frustration Simulation
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

// Adaptive Behavior
document.getElementById('completeTask').addEventListener('click', async () => {
    const response = await fetch('http://127.0.0.1:5000/api/adaptive', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user: 'default' })
    });
    const data = await response.json();
    document.getElementById('adaptiveMessage').innerText = data.message;
});

// Set initial theme
document.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('light');
    document.querySelector('header').classList.add('light');
    document.getElementById('chat-container').classList.add('light');
    document.getElementById('chat-box').classList.add('light');
    document.querySelector('textarea').classList.add('light');
    document.querySelectorAll('button').forEach(button => button.classList.add('light'));
    document.querySelectorAll('.dot').forEach(dot => dot.classList.add('light'));
    document.querySelectorAll('section').forEach(section => section.classList.add('light'));
    document.getElementById('theme-label').textContent = 'Light Mode';
});