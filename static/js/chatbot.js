function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    if (userInput.trim() === "") return;

    // Append user message
    chatBox.innerHTML += <div class="message user">${userInput}</div>;
    document.getElementById("user-input").value = "";

    // Send request to Flask server
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Append bot response
        chatBox.innerHTML += <div class="message bot">${data.response}</div>;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}