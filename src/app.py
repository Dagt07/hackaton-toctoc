from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

# Lista para almacenar el historial del chat
chat_history = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    global chat_history

    # Obtener el mensaje del usuario del cuerpo de la solicitud
    user_message = request.json.get("message", "")

    # Guardar el mensaje del usuario en el historial
    chat_history.append({"role": "user", "message": user_message})

    # Respuesta genérica del bot
    bot_response = "This is a generic response. Thank you for your message!"
    chat_history.append({"role": "bot", "message": bot_response})

    # Devolver la respuesta del bot como JSON
    return jsonify({"response": bot_response, "chat_history": chat_history})

if __name__ == "__main__":
    app.run(debug=True)
