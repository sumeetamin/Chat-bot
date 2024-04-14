document.getElementById('chat-form').onsubmit = function(e) {
    e.preventDefault();
    var userInput = document.getElementById('userInput');
    var chatbox = document.getElementById('chatbox');

    chatbox.innerHTML += `<div class="user-message">${userInput.value}</div>`;

    fetch("/get", {
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: "msg=" + encodeURIComponent(userInput.value)
    })
    .then(response => response.json())
    .then(data => {
        chatbox.innerHTML += `<div class="bot-message">${data.response}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch((error) => {
        console.error('Error:', error);
        chatbox.innerHTML += `<div class="bot-message">Sorry, I couldn't process that request.</div>`;
    });

    userInput.value = "";
};
