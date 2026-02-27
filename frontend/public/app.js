document.addEventListener('DOMContentLoaded', () => {
    const chatInput = document.querySelector('#chat-input');
    const sendButton = document.querySelector('#send-button');
    const chatMessages = document.querySelector('#chat-messages');

    sendButton.addEventListener('click', () => {
        const message = chatInput.value.trim();
        if (message) {
            displayMessage('You', message);
            chatInput.value = '';
            fetchChatResponse(message);
        }
    });

    function displayMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('chat-message');
        messageElement.textContent = `${sender}: ${message}`;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    async function fetchChatResponse(message) {
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });
            if (response.ok) {
                const data = await response.json();
                displayMessage('AI', data.response);
            } else {
                console.error('Error fetching chat response:', response.statusText);
            }
        } catch (error) {
            console.error('Error fetching chat response:', error);
        }
    }
});