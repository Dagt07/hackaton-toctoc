document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const chatBox = document.getElementById("chat-box");
    const userMessageInput = document.getElementById("user-message");

    // Manejar el envío del formulario
    chatForm.addEventListener("submit", async (e) => {
        e.preventDefault(); // Evitar que la página se recargue

        const userMessage = userMessageInput.value;

        if (!userMessage) return;

        // Mostrar el mensaje del usuario en el chat
        addMessage("user", userMessage);

        // Limpiar el campo de entrada
        userMessageInput.value = "";

        try {
            // Enviar el mensaje al servidor
            const response = await fetch("/send_message", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await response.json();

            // Mostrar la respuesta del bot en el chat
            addMessage("bot", data.response);
        } catch (error) {
            console.error("Error:", error);
        }
    });

    // Función para agregar mensajes al chat
    function addMessage(role, message) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add(role);
        messageDiv.innerHTML = `<strong>${role === "user" ? "You" : "Bot"}:</strong> ${message}`;
        chatBox.appendChild(messageDiv);

        // Desplazarse automáticamente hacia abajo
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
